import json
import os

from datetime import datetime

from models.tournament import Tournament
from models.round import Round
from models.player import Player

from views.tournamentview import TournamentView
from views.matchesview import MatchesView

from controllers.roundcontroller import RoundController


class TournamentController:
    def create_tournament(self):
        tournamentview = TournamentView()
        data = tournamentview.get_tournament_input_creation()
        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
        else:
            # Si le fichier n'existe pas, on initialise une liste vide
            tournaments = []

        # Ajoute le nouveau tournois à la liste
        tournaments.append(data)

        # Sauvegarde les données mises à jour dans le fichier JSON
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        tournament = Tournament(data["name"], data["location"], data["start_date"],
                                data["end_date"], data["rounds_number"])

        print("Le tournois a été crée avec succès.")
        print(tournament.name)

        self.save_tournament(tournament)
        return (tournament)

    # def instantiate_players(self, players, tournament):

    #     print (f"players: {players}")
    #     # Création des objets et récupération dans une liste
    #     players_in_tournament = [Player(**data) for data in players]
    #     #tournament.players = players_in_tournament
    #     tournament.players.append(players_in_tournament)
    #     return (players_in_tournament)

    def instantiate_player(self, player, tournament):

        tournament.players.append(Player(player["last_name"], player["first_name"],
                                         player["birth_date"], player["chess_id"]))
        return (player)

    def start_tournament(self, tournament):

        round = Round(tournament.current_round)
        round.start_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        roundcontroller = RoundController()
        roundcontroller.generate_round_matches(tournament, round)
        # Add round to tournament
        tournament.rounds.append(round)
        matchview = MatchesView()
        matchview.input_results(tournament)

        Player.sort_by_total_points(tournament)

        round.end_time = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Update current round in tournament
        tournament.current_round = tournament.current_round + 1


        return (tournament)

    def save_tournament(self, tournament):

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
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

                print(match[0][0].last_name)
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

        # Prepare the infos to be stored in a dict
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

        # Ajoute le nouveau tournois à la liste
        tournaments.append(dict_tournament_for_json)

        # Save updated date in JSON
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        print("Le tournois a été sauvegardé avec succès.")

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
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
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

                    print("nouveau match")

                    # Trouver tous les objets avec un nom donné

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
                                ['rounds_number'],
                                tournaments[tournament_number - 1]['current_round'],
                                rounds, players, tournaments[tournament_number - 1]['description'], )

        print("Le tournois a été chargé avec succès.")

        return (tournament)

    def tournament_status(self, tournament):
        tournament_ready = True
        error_code = 0

        if not tournament:
            print("Il n'existe pas de tournoi à lancer. Merci de crée ou charger un tournoi")
            tournament_ready = False
            error_code = 1
        else:
            if not tournament.players:
                print("Pas de joueurs dans le tournois. Merci d'ajouter des joueurs")
                tournament_ready = False
                error_code = 2
            elif len(tournament.players) % 2 != 0:
                print("Nombre de joueurs impair. Merci d'ajouter un joueur")
                tournament_ready = False
                error_code = 3

            # Test if there are still rounds to play
            if tournament.current_round + 1 >= tournament.rounds_number:
                print("Le tournoi est terminé")
                tournament_ready = False
                error_code = 4
            print(f"len(tournament.players): {len(tournament.players)}, rounds_number: {tournament.rounds_number}")
            if len(tournament.players) < tournament.rounds_number:
                print("Trop de rounds: impossible de n'avoir que des matchs uniques")
                tournament_ready = False
                error_code = 5

        return (tournament_ready, error_code)
