import json
import os
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

        print("Le joueur a été ajouté avec succès.")
        return (data)

    # def get_players_list(self):
    #     file_path = "data/players/players.json"
    #     # Open file JSON
    #     with open(file_path, 'r') as f:
    #         # Load JSON in a list
    #         players = json.load(f)

    #     sorted_players = sorted(players, key=lambda x: (x['last_name'].lower(), x['first_name'].lower()))

    #     # Access dictonary in list
    #     number = 1
    #     for player in sorted_players:
            
    #         print(f'{number}. {player["first_name"]} {player["last_name"]}, date de naissance: {player["birth_date"]}, chess ID: {player["chess_id"]}')
    #         number = number + 1

    #     # return list of dictionnaries contained in the json file
    #     return (players)
    
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
            return(None)
