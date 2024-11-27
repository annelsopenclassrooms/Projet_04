from models.tournament import Tournament
from controllers.inputcontroller import InputController
import os
import json

class TournamentView:
    def get_tournament_input_creation(self):
        dict_tournament_for_json = {}

        while True:
            tournament_name = input("Nom du tounois ?: ")
            if InputController.is_tournament_name(tournament_name):
                break
            else:
                print("Merci de donner un nom de tournois valide")
        dict_tournament_for_json["name"] = tournament_name
        
        while True:
            location_name = input("Nom du lieux ?: ")
            if InputController.is_location_name(location_name):
                break
            else:
                print("Merci de donner un nom de lieu valide")

        dict_tournament_for_json["location"] = location_name

        while True:
            start_date = input("Date de début ?: ")
            if InputController.is_date_past(start_date):
                break
            else:
                print("Merci de donner une date valide (JJ/MM/AAAA) et pas dans le futur")

        dict_tournament_for_json["start_date"] = start_date

        while True:
            end_date = input("Date de fin ?: ")
            if InputController.is_date(end_date):
                
            
                if end_date < start_date:
                    print("Le date de fin ne doit pas preceder la date de debut")
                else:
                    break
                
            else:
                print("Merci de donner une date valide (JJ/MM/AAAA) et apres ou le jour de la date de debut")

        dict_tournament_for_json["end_date"] = end_date

        while True:
            try:
                round_number = int(input("Nombre de tours ?: "))
                break
            except ValueError:
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")
        
        dict_tournament_for_json["rounds_number"] = round_number
        return (dict_tournament_for_json)

    def display_tournament_infos(self, tournament):
        print("tous les tournois (tournamentview, def display tournament info)")
        print(tournament)

    def display_ranking(self, tournament):
        players = tournament.players
        print("Classement actuel:")
        for player in players:
            print(f"{player.last_name} {player.first_name} {player.total_points} points")

    def list_tournament_from_json(self):
        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
        tournament_number = 1
        for tournament in tournaments:
            print (f"{tournament_number}. {tournament['name']} à {tournament['location']} le {tournament['start_date']}")
            tournament_number = tournament_number + 1

        


