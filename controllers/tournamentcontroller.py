import json
import os
from views.tournamentview import TournamentView
from views.playerview import PlayerView
from models.player import Player
from models.tounament import Tournament
from models.round import Round
from views.matchesview import MatchesView


class TournamentController:
    def create_tournament(self):
        c = TournamentView()
        
        data = c.get_tournament_input_creation()

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

        return(tournament)

    def instantiate_players(self, players):

        # Création des objets et récupération dans une liste
        players_in_tournament = [Player(**data) for data in players]

        Tournament.all[0].players = players_in_tournament
        #Tournament.all[0].players.append(players_in_tournament)

        # Accéder à la liste des objets
        print("Liste des objets :", players_in_tournament)

        # Accéder à un objet spécifique
        #print("Premier objet :", players_in_tournament[0])

        return (players_in_tournament)

       
    def start_tournament(self):
        
        r = Round(Tournament.all[0].current_round)
        r.generate_round1_matches()
        Tournament.all[0].rounds.append(r)
        print(Tournament.all[0])
        
        #Tournament.all[0].rounds.append(Round.round1_matches())
        #print(Tournament.all[0])
        m = MatchesView()
        m.input_results()


        Player.sort_by_total_points()

        print("Classement actuel")
        TournamentView.display_ranking()


        #Set 1 to current round in tournament
        Tournament.all[0].current_round = 1

        r = Round(Tournament.all[0].current_round)   
        r.generate_round()

        #add round to tournament
        Tournament.all[0].rounds.append(r)
        


        exit()