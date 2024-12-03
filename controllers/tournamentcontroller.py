import json
import os

from datetime import datetime
from rich import print

from models.tournament import Tournament
from models.round import Round
from models.player import Player

from views.tournamentview import TournamentView

from controllers.roundcontroller import RoundController
from controllers.matchcontroller import MatchesController


class TournamentController:
    def create_tournament(self):
        tournamentview = TournamentView()
        data = tournamentview.get_tournament_input_creation()
        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Load file if existing
            with open(file_path, "r") as f:
                tournaments = json.load(f)
        else:
            # If the file does not exist initialize empty list
            tournaments = []

        # Add tournament to the list
        tournaments.append(data)

        # Save updated data in the JSON file
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)

        tournament = Tournament(data["name"], data["location"], data["start_date"],
                                data["end_date"], data["rounds_number"], data["description"])

        print("[green]Le tournois a été crée avec succès.[/green]")

        self.save_tournament(tournament)
        return (tournament)

    def instantiate_player(self, player, tournament):

        tournament.players.append(Player(player["last_name"], player["first_name"],
                                         player["birth_date"], player["chess_id"]))
        print(f"[green]{player['first_name']} {player['last_name']} a été ajouté au tournois[/green]")

        return (player)

    def start_tournament(self, tournament):

        print(f"[dark_blue]Tour en cours: [/dark_blue]{tournament.current_round + 1}")

        matchcontroller = MatchesController()
        tournamentcontroller = TournamentController()

        round = Round(tournament.current_round)

        round.start_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        roundcontroller = RoundController()

        # if matches already created (loading an existing tournament)
        if len(tournament.rounds) >= tournament.current_round + 1:
            pass

        else:

            roundcontroller.generate_round_matches(tournament, round)

            # Add round to tournament
            tournament.rounds.append(round)

        # Get match results

        matches = tournament.rounds[tournament.current_round].matches
        for match in matches:
            # if match already resolve get next
            if matchcontroller.match_is_played(match):
                pass
            else:
                matchcontroller.get_results(match)

            # Save tournament
            tournamentcontroller.save_tournament(tournament)

        Player.sort_by_total_points(tournament)

        round.end_time = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Update current round in tournament
        tournament.current_round = tournament.current_round + 1

        # Save tournament
        tournamentcontroller.save_tournament(tournament)

        return (tournament)

    def save_tournament(self, tournament):

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Load file if existing
            with open(file_path, "r") as f:
                # Load existing data in a list
                tournaments = json.load(f)

        tournaments.pop(len(tournaments) - 1)

        # Prepare rounds to be stored in a list of dictionnaries
        rounds = []
        players = []
        for round in tournament.rounds:
            round_to_dict = {}
            round_to_dict["name"] = round.name
            round_to_dict["start_time"] = round.start_time
            round_to_dict["end_time"] = round.end_time

            # Prepare matches to be stored in a list
            matches = []
            for match in round.matches:
                player1_to_dict = {}
                player2_to_dict = {}

                player1_to_dict["last_name"] = match[0][0].last_name
                player1_to_dict["first_name"] = match[0][0].first_name
                player1_to_dict["birth_date"] = match[0][0].birth_date
                player1_to_dict["chess_id"] = match[0][0].chess_id
                player1_to_dict["total_points"] = match[0][0].total_points
                player1_to_dict["match_points"] = match[0][1]

                player2_to_dict["last_name"] = match[1][0].last_name
                player2_to_dict["first_name"] = match[1][0].first_name
                player2_to_dict["birth_date"] = match[1][0].birth_date
                player2_to_dict["chess_id"] = match[1][0].chess_id
                player2_to_dict["total_points"] = match[1][0].total_points
                player2_to_dict["match_points"] = match[1][1]

                matches.append([player1_to_dict, player2_to_dict])

            round_to_dict["matches"] = matches
            rounds.append(round_to_dict)
            players = []

        for player in tournament.players:
            player_to_dict = {}
            player_to_dict["last_name"] = player.last_name
            player_to_dict["first_name"] = player.first_name
            player_to_dict["birth_date"] = player.birth_date
            player_to_dict["chess_id"] = player.chess_id
            player_to_dict["total_points"] = player.total_points
            players.append(player_to_dict)

        # Prepare data to be stored in a dict
        dict_tournament_for_json = {}
        dict_tournament_for_json["name"] = tournament.name
        dict_tournament_for_json["location"] = tournament.location
        dict_tournament_for_json["start_date"] = tournament.start_date
        dict_tournament_for_json["end_date"] = tournament.end_date
        dict_tournament_for_json["rounds_number"] = tournament.rounds_number
        dict_tournament_for_json["current_round"] = tournament.current_round
        dict_tournament_for_json["rounds"] = rounds
        dict_tournament_for_json["players"] = players
        dict_tournament_for_json["description"] = tournament.description

        # Add new tournament to the list
        tournaments.append(dict_tournament_for_json)

        # Save updated date in JSON
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)

        print("[green]Le tournois a été sauvegardé avec succès.[/green]")

        return (tournament)

    def load_tournament(self):

        tournamentview = TournamentView()
        tournamentview.list_tournament_from_json()

        while True:
            try:
                tournament_number = int(input("Choisissez le tournois à charger: "))
                print(f"Merci ! Vous avez entré : {tournament_number}")
                break
            except ValueError:
                print("[red]ERREUR: Ce n'est pas un entier valide. Veuillez réessayer.[/red]")

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Load existing data in a list
            with open(file_path, "r") as f:
                tournaments = json.load(f)
        else:
            print("Aucun tournois sauvegardés")
            return (None)
        players = []

        if 'players' in tournaments[tournament_number - 1] and tournaments[tournament_number - 1]['players']:
            players_in_tournament = tournaments[tournament_number - 1]['players']
            for player in players_in_tournament:
                players.append(Player(player["last_name"], player["first_name"],
                                      player["birth_date"], player["chess_id"], player["total_points"]))

        rounds = []
        if 'rounds' in tournaments[tournament_number - 1] and tournaments[tournament_number - 1]['rounds']:

            rounds_in_tournament = tournaments[tournament_number - 1]['rounds']

            for round in rounds_in_tournament:
                # Get matches
                matches = []
                for match in round["matches"]:

                    # Find object player with chess_id
                    chess_id_player1 = match[0]['chess_id']
                    chess_id_player2 = match[1]['chess_id']
                    player1 = next((player for player in players if player.chess_id == chess_id_player1), None)
                    player2 = next((player for player in players if player.chess_id == chess_id_player2), None)

                    match_to_add = ([player1, match[0]['match_points']], [player2, match[1]['match_points']])
                    matches.append(match_to_add)

                round_to_add = Round(round["name"])
                round_to_add.start_time = round["start_time"]
                round_to_add.end_time = round["end_time"]
                round_to_add.matches = matches

                rounds.append(round_to_add)

        tournament = Tournament(tournaments[tournament_number - 1]['name'], tournaments[tournament_number - 1]
                                ['location'], tournaments[tournament_number - 1]['start_date'],
                                tournaments[tournament_number - 1]['end_date'], tournaments[tournament_number - 1]
                                ['rounds_number'], tournaments[tournament_number - 1]['description'], )

        tournament.current_round = tournaments[tournament_number - 1]['current_round']
        tournament.rounds = rounds
        tournament.players = players

        print("[green]Le tournois a été chargé avec succès.[/green]")

        if tournament.current_round >= tournament.rounds_number:
            print("[dark_orange]Le tournois est terminé.[/dark_orange]")

        return (tournament)

    def tournament_status(self, tournament):
        tournament_ready = True
        error_code = 0

        if not tournament:
            print("[red]ERREUR: Il n'existe pas de tournoi à lancer. Merci de crée ou charger un tournoi[/red]")
            tournament_ready = False
            error_code = 1
        else:
            if not tournament.players:
                print("[red]ERREUR: Pas de joueurs dans le tournois. Merci d'ajouter des joueurs[/red]")
                tournament_ready = False
                error_code = 2
            elif len(tournament.players) % 2 != 0:
                print("[red]ERREUR: Nombre de joueurs impair. Merci d'ajouter un joueur[/red]")
                tournament_ready = False
                error_code = 3

            # Test if there are still rounds to play
            if tournament.current_round + 1 >= tournament.rounds_number:
                print("[red]ERREUR: Le tournoi est terminé[/red]")
                tournament_ready = False
                error_code = 4

            if len(tournament.players) < tournament.rounds_number:
                print("[red]ERREUR: Trop de rounds: impossible de n'avoir que des matchs uniques.[/red]")
                tournament_ready = False
                error_code = 5

        return (tournament_ready, error_code)

    def change_round_number(self, tournament, new_round_number):
        tournamentcontroller = TournamentController()

        tournament.rounds_number = new_round_number

        print(tournament)

        tournamentcontroller.save_tournament(tournament)
