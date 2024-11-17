import json
import os
# from models.player import Player
from views.createplayerview import CreatePlayerView


class PlayerController:
    def create_player():
        c = CreatePlayerView()
        data = c.input_player_info()

        if os.path.exists("test.json"):
            # Si le fichier existe, on le charge
            with open("test.json", "r") as f:
                players = json.load(f)  # Charge les données existantes dans une liste
        else:
            # Si le fichier n'existe pas, on initialise une liste vide
            players = []

        # Ajoute le nouveau joueur à la liste
        players.append(data)

        # Sauvegarde les données mises à jour dans le fichier JSON
        with open("test.json", "w") as f:
            json.dump(players, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        print("Le joueur a été ajouté avec succès.")

    def add_player_to_tournament():
        pass

    def get_player_list():
        pass
