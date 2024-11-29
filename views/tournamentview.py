import os
import json

from rich.console import Console
from rich.table import Table

from controllers.inputcontroller import InputController


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

        tournament_description = input("Description du tounois ?(pas obligatoire): ")
        dict_tournament_for_json["description"] = tournament_description

        return (dict_tournament_for_json)

    def display_tournament_infos(self, tournament):

        print(tournament)
        print(tournament.players)
        table = Table(title="Infos du tournois", show_header=False, show_lines=True)

        # Define additional columns for data
        table.add_column("Value 1", style="bold")
        table.add_column("Value 2", style="dark_blue")

        table.add_row("Nom", tournament.name)
        table.add_row("Lieu", tournament.location)
        table.add_row("Date de début", tournament.start_date)
        table.add_row("Date de fin", tournament.end_date)
        table.add_row("Description", str(tournament.description))
        table.add_row("Nombre de round", str(tournament.rounds_number))
        table.add_row("Nombre de round joués", str(tournament.current_round))
        table.add_row("Nombre de joueurs", str(len(tournament.players)))

        console = Console()
        console.print(table)
        print(tournament)

    def display_ranking(self, tournament):
        players = tournament.players
        
        # use Rich module to print a table
        table = Table(title="Classement des joueurs")

        table.add_column("Nom", style="purple3")
        table.add_column("Prénom", style="cyan")
        table.add_column("Points", style="dark_blue")

        for player in players:
            table.add_row(str(player.first_name), str(player.last_name), str(player.total_points))

        console = Console()
        console.print(table)

    def list_tournament_from_json(self):
        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste

        # use Rich module to print a table
        table = Table(title="Liste des tournois")
        table.add_column("Numéro", style="cyan")
        table.add_column("Nom", style="purple3")
        table.add_column("Lieux", style="magenta")
        table.add_column("Date de début", style="green")
        tournament_number = 1
        for tournament in tournaments:

            table.add_row(str(tournament_number), str(tournament['name']), str(tournament['location']),
                          str(tournament['start_date']))

            tournament_number = tournament_number + 1

        console = Console()
        console.print(table)

    def display_tournament_name_date(self, number):
        file_path = "data/tournaments/tournaments.json"

        print("display_tournament_name_date")

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste

        tournament = tournaments[number]

        # use Rich module to print a table
        table = Table(title="Détails du tournoi")
        table.add_column("Nom", style="purple3")
        table.add_column("Date de début", style="green")
        table.add_column("Date de fin", style="magenta")

        table.add_row(str(tournament['name']), str(tournament['start_date']),
                      str(tournament['end_date']))

        console = Console()
        console.print(table)

    def display_tournament_players_list(self, number):

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)

        players = tournaments[number - 1]["players"]

        sorted_players = sorted(players, key=lambda x: (x['last_name'].lower(), x['first_name'].lower()))

        # use Rich module to print a table
        table = Table(title="Liste des joueurs dans le tournois")

        table.add_column("Nom", style="purple3")
        table.add_column("Prénom", style="cyan")

        for player in sorted_players:
            table.add_row(str(player['first_name']), str(player['last_name']))

        console = Console()
        console.print(table)

    # 3. Liste de tous les tours du tournoi et de tous les matchs du tour
    def display_tournament_rounds(self, number):

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste

        # use Rich module to print a table
        round_number = 1
        for round in tournaments[number - 1]["rounds"]:

            table = Table(title=f"Tour: {round_number}")
            table.add_column("Joueur 1", style="cyan")
            table.add_column("Score", style="dodger_blue1")
            table.add_column("Joueur 2", style="green4")
            table.add_column("Score", style="green")

            for match in round["matches"]:
                table.add_row(str(f"{match[0]['first_name']} {match[0]['last_name']}"), str(match[0]['match_points']),
                              str(f"{match[1]['first_name']} {match[1]['last_name']}"), str(match[1]['match_points']))
            round_number = round_number + 1

            console = Console()
            console.print(table)

    def display_players_in_current_tournament(self, tournament):

        table = Table(title="Liste des joueurs dans le tournois en cours")

        table.add_column("Nom", style="purple3")
        table.add_column("Prénom", style="cyan")

        for player in tournament.players:
            table.add_row(str(player.first_name), str(player.last_name))

        console = Console()
        console.print(table)