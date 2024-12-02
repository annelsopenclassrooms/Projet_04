import json
from rich import print
from rich.console import Console
from rich.table import Table
from controllers.inputcontroller import InputController


class PlayerView:
    def get_player_input(self):
        dict_infos = {}

        while True:
            last_name = input("Nom de famille du joueur? : ")
            if InputController.is_last_name(last_name):
                break
            else:
                print("[red]ERREUR: Merci de donner un nom de famille valide[/red]")
        dict_infos["last_name"] = last_name

        while True:
            first_name = input("Prénom du joueur? : ")
            if InputController.is_first_name(first_name):
                break
            else:
                print("[red]ERREUR: Merci de donner un prénom valide[/red]")

        dict_infos["first_name"] = first_name

        while True:
            birth_date = input("Date de naissance du joueur? : ")
            if InputController.is_date(birth_date):
                break
            else:
                print("[red]ERREUR: Merci de donner une date valide et pas dans le futur[/red]")
        dict_infos["birth_date"] = birth_date

        while True:
            chess_id = input("Identifiant du joueur? : ")
            if InputController.is_valid_id_chess(chess_id):
                break
            else:
                print("[red]ERREUR: Merci de donner un identifiant valide ex:AB12345[/red]")

        dict_infos["chess_id"] = chess_id

        return (dict_infos)

    def get_players_list(self):
        file_path = "data/players/players.json"
        # Open file JSON
        with open(file_path, 'r') as f:
            # Load JSON in a list
            players = json.load(f)

        sorted_players = sorted(players, key=lambda x: (x['last_name'].lower(), x['first_name'].lower()))

        # use Rich module to print a table
        table = Table(title="Liste des joueurs")
        table.add_column("Numéro", style="cyan")
        table.add_column("Prénom", style="purple3")
        table.add_column("Nom", style="magenta")
        table.add_column("Date de naissance", style="green")
        table.add_column("Chess ID", style="chartreuse2")
        number = 1
        for player in sorted_players:

            table.add_row(str(number), str(player['first_name']), str(player['last_name']),
                          str(player['birth_date']), str(player['chess_id']))

            number = number + 1

        console = Console()
        console.print(table)

        # Return list of dictionnaries contained in the json file
        return (sorted_players)
