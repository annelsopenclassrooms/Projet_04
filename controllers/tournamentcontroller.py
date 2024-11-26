import json
import os
from views.tournamentview import TournamentView
from views.playerview import PlayerView
from views.matchesview import MatchesView
from models.tournament import Tournament
from models.round import Round
from models.player import Player



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

        tournament = Tournament(data["name"], data["location"], data["start_date"], data["end_date"], data["rounds_number"])

        print("Le tournois a été crée avec succès.")
        print(tournament.name)

        return (tournament)

    def instantiate_players(self, players, tournament):

        # Création des objets et récupération dans une liste
        players_in_tournament = [Player(**data) for data in players]
        tournament.players = players_in_tournament
        return (players_in_tournament)

    def start_tournament(self, tournament):

        while True:
            round = Round(tournament.current_round)
            round.generate_round_matches(tournament)
            # add round to tournament
            tournament.rounds.append(round)
            matchview = MatchesView()
            matchview.input_results(tournament)

            Player.sort_by_total_points(tournament)

            print("Classement actuel")
            TournamentView.display_ranking(tournament)

            # Update current round in tournament
            tournament.current_round = tournament.current_round + 1
            
            print (f"Depuis start tournament: round en cours {tournament.current_round}, nombre de tours{tournament.rounds_number}")
            if tournament.current_round >= tournament.rounds_number:

                for round in tournament.rounds:
                    for match in round.matches:
                        print (f"round: {round.name}: {match[0][0].first_name} vs {match[1][0].first_name}")

                break


