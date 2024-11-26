import json
import os
from views.playerview import PlayerView


class PlayerController:
    def create_player(self):
        playerview = PlayerView()
        data = playerview.get_player_input()

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
        return (data)

    def get_players_list(self):
        # Ouvrir le fichier JSON
        with open('test.json', 'r') as f:
            # Charger les données JSON dans une liste
            data = json.load(f)

        # Afficher les données (qui sont une liste de dictionnaires)
        #print(data)

        # Accéder à chaque dictionnaire dans la liste
        number = 1
        for dict in data:
            
            print(f'{number}. {dict["first_name"]} {dict["last_name"]}, date de naissance: {dict["birth_date"]}, chess ID: {dict["chess_id"]}')
            number = number + 1

        # return list of dictionnaries contained in the json file
        return (data)
    
    def search_chess_id(self, chess_id):
        with open('test.json', 'r') as f:
            data = json.load(f)

        found = False

        for entry in data:
            if entry.get("chess_id") == chess_id:
                print(f'La valeur "{chess_id}" a été trouvée dans le dictionnaire: {entry}')
                return (entry)
                
        if not found:
            print(f'La valeur "{chess_id}" n\'a pas été trouvée.')
            return(None)
