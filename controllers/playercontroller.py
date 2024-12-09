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
            # Load file if existing
            with open(file_path, "r") as f:
                players = json.load(f)
        else:
            # If the file does not exist initialize empty list
            players = []

        # Add new player to the list
        players.append(data)

        # Save updated data in the JSON file
        with open(file_path, "w") as f:
            json.dump(players, f, indent=4)

        print("[green]Le joueur a été ajouté avec succès.[green]")
        return (data)

    def search_chess_id(self, chess_id):
        file_path = "data/players/players.json"

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"[red]ERREUR : Le fichier '{file_path}' est introuvable.[/red]")
            return (None)
        except json.JSONDecodeError:
            print(f"[red]ERREUR : Le fichier '{file_path}' contient des données JSON non valides.[/red]")
            return (None)

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
