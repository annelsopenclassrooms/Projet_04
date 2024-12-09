import os
import json
import csv

from datetime import datetime

from rich import print
from rich.console import Console
from rich.table import Table

from controllers.inputcontroller import InputController


class TournamentView:
    def get_tournament_input_creation(self):
        dict_tournament_for_json = {}
        inputcontroller = InputController()

        while True:
            tournament_name = input("Nom du tournois ?: ")
            if inputcontroller.is_tournament_name(tournament_name):
                break
            else:
                print("Merci de donner un nom de tournois valide")
        dict_tournament_for_json["name"] = tournament_name

        while True:
            location_name = input("Nom du lieux ?: ")
            if inputcontroller.is_location_name(location_name):
                break
            else:
                print("Merci de donner un nom de lieu valide")

        dict_tournament_for_json["location"] = location_name

        while True:
            start_date = input("Date de début ?: ")
            if inputcontroller.is_date_past(start_date):
                break
            else:
                print("Merci de donner une date valide (JJ/MM/AAAA) et pas dans le futur")

        dict_tournament_for_json["start_date"] = start_date

        while True:
            end_date = input("Date de fin ?: ")
            if inputcontroller.is_date(end_date):

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
                print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

        dict_tournament_for_json["rounds_number"] = round_number

        tournament_description = input("Description du tounois ?(pas obligatoire): ")
        dict_tournament_for_json["description"] = tournament_description

        return (dict_tournament_for_json)

    def display_tournament_infos(self, tournament):

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
        table_to_export = []

        try:
            with open(file_path, 'r') as f:
                tournaments = json.load(f)
        except FileNotFoundError:
            print(f"[red]ERREUR : Le fichier '{file_path}' est introuvable.[/red]")
            return (None)
        except json.JSONDecodeError:
            print(f"[red]ERREUR : Le fichier '{file_path}' contient des données JSON non valides.[/red]")
            return (None)

        # prepare for export
        title = ["Numéro", "Nom", "Lieux", "Date de début"]
        table_to_export.append(title)

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

            table_to_export.append([tournament_number, tournament['name'], tournament['location'],
                                    tournament['start_date']])

            tournament_number = tournament_number + 1

        console = Console()
        console.print(table)
        return (table_to_export)

    def display_tournament_name_date(self, number):
        file_path = "data/tournaments/tournaments.json"
        table_to_export = []

        if os.path.exists(file_path):
            # Load file if existing
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste

        tournament = tournaments[number - 1]

        # prepare for export
        title = ["Nom", "Lieux", "Date de début", "Date de fin"]
        table_to_export.append(title)

        # use Rich module to print a table
        table = Table(title="Détails du tournoi")
        table.add_column("Nom", style="purple3")
        table.add_column("Lieu", style="medium_orchid")
        table.add_column("Date de début", style="green")
        table.add_column("Date de fin", style="magenta")

        table.add_row(str(tournament['name']), str(tournament['location']), str(tournament['start_date']),
                      str(tournament['end_date']))

        table_to_export.append([tournament['name'], tournament['location'],
                                tournament['start_date'], tournament['end_date']])

        console = Console()
        console.print(table)
        return (table_to_export, tournament['name'])

    def display_tournament_players_list(self, number):

        file_path = "data/tournaments/tournaments.json"
        table_to_export = []

        if os.path.exists(file_path):
            # Load file if existing
            with open(file_path, "r") as f:
                tournaments = json.load(f)

        players = tournaments[number - 1]["players"]

        sorted_players = sorted(players, key=lambda x: (x['last_name'].lower(), x['first_name'].lower()))

        # prepare for export
        title = ["Prénom", "Nom"]
        table_to_export.append(title)
        file_title = tournaments[number - 1]["name"]

        # use Rich module to print a table
        table = Table(title="Liste des joueurs dans le tournois")

        table.add_column("Prénom", style="purple3")
        table.add_column("Nom", style="cyan")

        for player in sorted_players:
            table.add_row(str(player['first_name']), str(player['last_name']))

            table_to_export.append([player['first_name'], player['last_name']])

        console = Console()
        console.print(table)
        return (table_to_export, file_title)

    # 3. Liste de tous les tours du tournoi et de tous les matchs du tour
    def display_tournament_rounds(self, number):

        file_path = "data/tournaments/tournaments.json"
        table_to_export = []

        if os.path.exists(file_path):
            # Load file if existing
            with open(file_path, "r") as f:
                tournaments = json.load(f)

        # prepare for export
        title = ["Tour", "Prénom joueur 1", "Nom Joueur 1", "Prénom joueur 2", "Score joueur 1",
                 "Prénom joueur 2", "Nom Joueur 2", "Score joueur 2"]
        table_to_export.append(title)

        file_title = tournaments[number - 1]["name"]

        # use Rich module to print a table
        round_number = 1

        tournaments[number - 1]["rounds"]
        for round in tournaments[number - 1]["rounds"]:

            table = Table(title=f"Tour: {round_number}")
            table.add_column("Joueur 1", style="cyan")
            table.add_column("Score", style="dodger_blue1")
            table.add_column("Joueur 2", style="green4")
            table.add_column("Score", style="green")

            for match in round["matches"]:
                table.add_row(str(f"{match[0]['first_name']} {match[0]['last_name']}"), str(match[0]['match_points']),
                              str(f"{match[1]['first_name']} {match[1]['last_name']}"), str(match[1]['match_points']))

                table_to_export.append([round_number, match[0]['first_name'], match[0]['last_name'],
                                        match[0]['match_points'],
                                        match[1]['first_name'], match[1]['last_name'], match[1]['match_points']])
            round_number = round_number + 1

            console = Console()
            console.print(table)

        return (table_to_export, file_title)

    def display_players_in_current_tournament(self, tournament):

        table = Table(title="Liste des joueurs dans le tournois en cours")

        table.add_column("Prénom", style="purple3")
        table.add_column("Nom", style="cyan")

        for player in tournament.players:
            table.add_row(str(player.first_name), str(player.last_name))

        console = Console()
        console.print(table)

    def export(self, table, title):

        # Create 'export' directory if it doesn't exist
        if not os.path.exists('export'):
            os.makedirs('export')

        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Use the title and date/time in the filename
        filename = f"export/{title}_{current_datetime}.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(table)  # Écrire toutes les lignes dans le fichier CSV
        print(f"[green]Le fichier CSV a été généré : {filename}[/green]")

    def input_round_number(self, tournament):
        while True:
            try:
                round_number = int(input("Nombre de tours ?: "))
                break
            except ValueError:
                print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

        return (round_number)
