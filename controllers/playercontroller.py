import json
import os

from rich import print

from views.playerview import PlayerView


class PlayerController:
    def create_player(self):
        playerview = PlayerView()
        data = playerview.get_player_input()
        file_path = "data/players/players.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                players = json.load(f)  # Charge les données existantes dans une liste
        else:
            # Si le fichier n'existe pas, on initialise une liste vide
            players = []

        # Ajoute le nouveau joueur à la liste
        players.append(data)

        # Sauvegarde les données mises à jour dans le fichier JSON
        with open(file_path, "w") as f:
            json.dump(players, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        print("[green]Le joueur a été ajouté avec succès.[green]")
        return (data)

    def search_chess_id(self, chess_id):
        file_path = "data/players/players.json"
        with open(file_path, 'r') as f:
            data = json.load(f)

        found = False

        for entry in data:
            if entry.get("chess_id") == chess_id:
                print(f'La valeur "{chess_id}" a été trouvée dans le dictionnaire: {entry}')
                return (entry)

        if not found:
            print(f'La valeur "{chess_id}" n\'a pas été trouvée.')
            return (None)

    def is_player_in_tournament(self, player, tournament):

        # Return True if chess_id found in existing tournament player else false

        chess_id = player["chess_id"]
        return any(p.chess_id == chess_id for p in tournament.players)
