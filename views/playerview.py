import json
from controllers.inputcontroller import InputController


class PlayerView:
    def get_player_input(self):
        dict_infos = {}

        while True:
            last_name = input("Nom de famille du joueur? : ")
            if InputController.is_last_name(last_name):
                break
            else:
                print("Merci de donner un nom de famille valide")
        dict_infos["last_name"] = last_name

        while True:
            first_name = input("Prénom du joueur? : ")
            if InputController.is_first_name(first_name):
                break
            else:
                print("Merci de donner un prénom valide")

        dict_infos["first_name"] = first_name

        while True:
            birth_date = input("Date de naissance du joueur? : ")
            if InputController.is_date(birth_date):
                break
            else:
                print("Merci de donner une date valide et pas dans le futur")
        dict_infos["birth_date"] = birth_date

        while True:
            chess_id = input("Identifiant du joueur? : ")
            if InputController.is_valid_id_chess(chess_id):
                break
            else:
                print("Merci de donner un identifiant valide ex:AB12345")

        dict_infos["chess_id"] = chess_id

        return (dict_infos)

    def get_players_list(self):
        file_path = "data/players/players.json"
        # Open file JSON
        with open(file_path, 'r') as f:
            # Load JSON in a list
            players = json.load(f)

        sorted_players = sorted(players, key=lambda x: (x['last_name'].lower(), x['first_name'].lower()))

        # Access dictonary in list
        number = 1
        for player in sorted_players:

            print(
                f"{number}. {player['first_name']} {player['last_name']}, "
                f"date de naissance: {player['birth_date']}, "
                f"chess ID: {player['chess_id']}"
                )
            number = number + 1

        # Return list of dictionnaries contained in the json file
        return (sorted_players)
