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

        if os.path.exists("test-tournament.json"):
            # Si le fichier existe, on le charge
            with open("test-tournament.json", "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
        else:
            # Si le fichier n'existe pas, on initialise une liste vide
            tournaments = []

        # Ajoute le nouveau tournois à la liste
        tournaments.append(data)

        # Sauvegarde les données mises à jour dans le fichier JSON
        with open("test-tournament.json", "w") as f:
            json.dump(tournaments, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        tournament = Tournament(data["name"], data["location"], data["start_date"], data["rounds_number"])

        print("Le tournois a été crée avec succès.")
        print(tournament.name)

        return (tournament)

    def instantiate_players(self, players, tournament):

        # Création des objets et récupération dans une liste
        players_in_tournament = [Player(**data) for data in players]
        tournament.players = players_in_tournament
        return (players_in_tournament)

    def start_tournament(self, tournament):

        round = Round(tournament.current_round)
        round.generate_round_matches(tournament)
        tournament.rounds.append(round)
        matchview = MatchesView()
        matchview.input_results(tournament)

        #Player.sort_by_total_points(tournament)

        print("Classement actuel")
        TournamentView.display_ranking(tournament)

####################################
#a factoriser


        # Set 1 to current round in tournament
        tournament.current_round = 1

        

        round = Round(tournament.current_round)   
        round.generate_round_matches(tournament)

        # add round to tournament
        tournament.rounds.append(round)

        matchview.input_results(tournament)

        print("Classement actuel")
        TournamentView.display_ranking(tournament)