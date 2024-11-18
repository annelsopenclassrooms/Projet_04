import json
import os
from views.tournamentview import TournamentView


class TournamentController:
    def create_tournament():
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

        print("Le tournois a été crée avec succès.")

    


        # class TournamentController {
        #     +create_tournament()
        #     +start_round()
        #     +end_round()
        #     +enter_results()
        #     +generate_pairs()
        # }