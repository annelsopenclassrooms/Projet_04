from controllers.playercontroller import PlayerController
from views.playerview import PlayerView
from rich import print


class MenuView:

    def main_menu(self):
        while True:
            print("[dark_blue]Menu Principal[/dark_blue]")
            print("1. Creer des joueurs")
            print("2. Tournois")
            print("3. Rapports")
            print("4. Quitter le programme")
            choice = input("choix ?:")

            return (choice)

    def tournament_menu(self):

        print("[dark_blue]Menu tournois[/dark_blue]")
        print("1. Charger un tournois")
        print("2. Creer un tournois")
        print("3. Ajouter des joueurs au tournois")
        print("4. Lancer/reprendre le tournois")
        print("5. Afficher les infos du tournois")
        print("6. Retour")
        choice = input("choix ?:")
        return (choice)

    def add_player_choice_list(self):

        print("[dark_blue]Ajouter un joueur au tournois:[/dark_blue]")
        print("1. Depuis la liste des joueurs existants")
        print("2. Depuis son chess ID")
        print("3. Creer un nouveau joueur et l'ajouter au tournois")
        print("4. Retour")
        choice = input("choix ?:")
        choice = int(choice)
        print(choice)

        return (choice)

    # choice 1
    def get_player_from_list(self):
        print("Liste des joueurs")
        playerview = PlayerView()
        players, table_to_export = playerview.get_players_list()

        if players:

            while True:
                try:
                    choice = int(input("choix ?:"))
                    print(f"Merci ! Vous avez entré : {choice}")
                    if len(players) < choice or choice == 0:
                        print("Merci d'entrer un valeur existante")
                    else:
                        break
                except ValueError:
                    print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            choice = choice - 1
            print(f"[green]Vous avez ajouté {players[choice]['first_name']} {players[choice]['last_name']}[/green]")

            return (players[choice])

        else:
            print("[red]ERREUR: Il n'y a aucun joueur enregistré.[/red]")
            return (None)

    # choice 2
    def get_player_from_chess_id(self):
        chess_id_searched = input("chess id?: ")
        playercontroller = PlayerController()
        result = playercontroller.search_chess_id(chess_id_searched)
        if result:
            return (result)
        else:
            print("[red]ERREUR: Joueur non trouvé[/red]")

    def next_round_menu(self):
        print("[dark_blue]Menu tour[/dark_blue]")
        print("1. Passer au tour suivant")
        print("2. Afficher le classement actuel")
        print("3. Retour")

        choice = input("choix ?:")
        return (choice)

    def rapport_menu(self):
        print("[dark_blue]Menu rapports[/dark_blue]")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Détails d'un tournois")
        print("4. Retour")

        choice = input("choix ?:")
        return (choice)

    def rapport_tournament_menu(self):
        print("[dark_blue]Menu rapport tournois[/dark_blue]")
        print("1. Nom et dates du tournoi donné")
        print("2. Liste des joueurs du tournoi par ordre alphabétique")
        print("3. Liste de tous les tours du tournoi et de tous les matchs du tour")
        print("4. Retour")

        choice = input("choix ?:")
        return (choice)

    def export_menu(self):
        print("[dark_blue]Voulez vous exporter le rapport ?[/dark_blue]")
        print("1. Oui")
        print("2. Non")

        choice = input("choix ?:")
        return (choice)

    def change_round_number_menu(self):
        print("[dark_blue]Voulez vous changer le nombre de tour ?[/dark_blue]")
        print("1. Oui")
        print("2. Non")

        choice = input("choix ?:")
        return (choice)
