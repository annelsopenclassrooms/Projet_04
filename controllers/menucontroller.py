
from rich import print

from views.tournamentview import TournamentView
from views.menuview import MenuView
from views.playerview import PlayerView

from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController


class MenuController:

    def launch_main_menu(self, tournament):
        menuview = MenuView()
        menucontroller = MenuController()
        while True:
            while True:
                try:
                    choice = int(menuview.main_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:
                # 1. Creer des joueurs
                case 1:
                    playercontroller = PlayerController()
                    playercontroller.create_player()
                # 2. Tournois
                case 2:
                    tournament = menucontroller.launch_tournament_menu(tournament)
                # 3. Rapports
                case 3:
                    menucontroller.launch_rapport_menu(tournament)
                # 4. Quitter le programme
                case 4:
                    print("BYE BYE")
                    exit()
                case _:
                    print("[red]ERREUR: Merci d'entre un valeur comprise entre 1 et 4[/red]")

    def launch_add_player_menu(self, tournament):
        menuview = MenuView()
        tournamentcontroller = TournamentController()
        playercontroller = PlayerController()
        tournamentview = TournamentView()
        menucontroller = MenuController()

        if not tournament:
            print("[red]ERREUR: Merci de créer ou charger un tournois avant d'ajouter les joueurs[/red]")
        else:
            while True:

                tournamentview.display_players_in_current_tournament(tournament)

                while True:
                    try:
                        choice = int(menuview.add_player_choice_list())
                        print(f"Merci ! Vous avez entré : {choice}")
                        break
                    except ValueError:
                        print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

                match choice:
                    case 1:
                        print("Ajouter un joueur depuis la liste des joueurs existants.")
                        player = menuview.get_player_from_list()
                        if playercontroller.is_player_in_tournament(player, tournament):
                            print("[red]ERREUR: Joueur.se déjà présent.e dans le tournois[/red]")
                        else:
                            tournamentcontroller.instantiate_player(player, tournament)
                            tournamentcontroller.save_tournament(tournament)

                    case 2:
                        print("Ajouter un joueur depuis son Chess ID.")
                        player = menuview.get_player_from_chess_id()
                        if playercontroller.is_player_in_tournament(player, tournament):
                            print("[red]ERREUR: Joueur.se déjà présent.e dans le tournois[/red]")
                        else:
                            tournamentcontroller.instantiate_player(player, tournament)
                            tournamentcontroller.save_tournament(tournament)
                    case 3:
                        print("Créer un nouveau joueur et l'ajouter au tournoi.")
                        playercontroller = PlayerController()
                        player = playercontroller.create_player()
                        if playercontroller.is_player_in_tournament(player, tournament):
                            print("[red]ERREUR: Joueur.se déjà présent.e dans le tournois[/red]")
                        else:
                            tournamentcontroller.instantiate_player(player, tournament)
                            tournamentcontroller.save_tournament(tournament)

                    case 4:
                        menucontroller.launch_tournament_menu(tournament)
                    case _:
                        print("[red]ERREUR: Choix invalide. Veuillez choisir une option entre 1 et 4.[/red]")
        return (tournament)

    def launch_tournament_menu(self, tournament):
        menuview = MenuView()
        tournamentcontroller = TournamentController()
        tournamentview = TournamentView()
        menucontroller = MenuController()

        while True:
            while True:
                try:
                    choice = int(menuview.tournament_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:
                # 1. Charger un tournois
                case 1:
                    if tournament:
                        print(
                            "[red]ERREUR: Un tournoi est déjà chargé. [/red]"
                            "Merci de quitter le logiciel si vous souhaitez en charger un autre."
                            )
                    else:
                        tournament = tournamentcontroller.load_tournament()

                # 2. Creer un tournois
                case 2:
                    if tournament:

                        print(
                            "[red]ERREUR: Un tournoi est déjà chargé. [/red]"
                            "Merci de quitter le logiciel si vous souhaitez en créer un nouveau."
                            )
                    else:
                        tournament = tournamentcontroller.create_tournament()

                # 3. Ajouter des joueurs au tournois
                case 3:
                    if len(tournament.rounds) != 0:
                        print("[red]ERREUR: Le tournois est déjà lancé. Impossible d'ajouter des joueurs[/red]")
                    else:
                        tournament = menucontroller.launch_add_player_menu(tournament)

                # 4. Lancer le tournois
                case 4:

                    tournament_status = tournamentcontroller.tournament_status(tournament)

                    if tournament_status[0]:
                        # Tournament ready
                        while True:
                            if tournament.current_round >= tournament.rounds_number:
                                menucontroller.launch_end_of_tournament_menu(tournament)
                                menucontroller.launch_main_menu(tournament)

                            else:
                                tournament = tournamentcontroller.start_tournament(tournament)
                                menucontroller.launch_next_round_menu(tournament)

                    if tournament_status[1] == 5:
                        menucontroller.launch_change_round_menu(tournament)

                    else:
                        print("Merci de corriger le problème avant de lancer le tournois")

                # 5. Afficher les infos du tournois
                case 5:
                    if tournament:
                        tournamentview.display_tournament_infos(tournament)
                    else:
                        print("[red]ERREUR: Aucun tournois en cours. Merci de créer ou charger un tournois[/red]")
                # 6. Retour
                case 6:
                    menucontroller.launch_main_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 6")

    def launch_next_round_menu(self, tournament):
        menuview = MenuView()
        tournamentview = TournamentView()

        while True:

            while True:
                try:
                    choice = int(menuview.next_round_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:

                # 1. Passer au tour suivant
                case 1:
                    return (tournament)
                # 2. Afficher le classement actuel
                case 2:
                    tournamentview.display_ranking(tournament)
                # 3. Retour
                case 3:
                    MenuController.launch_tournament_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 3")

    def launch_end_of_tournament_menu(self, tournament):
        print("♜♞♝♛♚♝♞♜ ♟♟♟♟♟♟♟♟ FIN DU TOURNOIS ♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜ ")
        tournamentview = TournamentView()
        tournamentview.display_ranking(tournament)
        return (tournament)

    def launch_rapport_menu(self, tournament):
        menuview = MenuView()
        tournamentview = TournamentView()
        menucontroller = MenuController()

        while True:
            while True:
                try:
                    choice = int(menuview.rapport_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:

                # 1. Liste de tous les joueurs par ordre alphabétique
                case 1:
                    playerview = PlayerView()
                    players, table_to_export = playerview.get_players_list()
                    menucontroller.launch_export_menu(table_to_export, "Liste_des_joueurs")
                # 2. Liste de tous les tournois
                case 2:
                    tournamentview = TournamentView()
                    table_to_export = tournamentview.list_tournament_from_json()
                    menucontroller.launch_export_menu(table_to_export, "Liste_des_tournois")

                # 3. Détails d'un tournois
                case 3:
                    tournamentview = TournamentView()
                    tournamentview.list_tournament_from_json()
                    menucontroller.launch_rapport_tournament_menu(tournament)
                # 4. Retour
                case 4:
                    menucontroller.launch_main_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 4")

    def launch_rapport_tournament_menu(self, tournament):
        menuview = MenuView()
        tournamentview = TournamentView()
        menucontroller = MenuController()

        while True:
            try:
                tournament_choice = int(input("Selectionnez un tournois: "))
                print(f"Merci ! Vous avez entré : {tournament_choice}")
                break
            except ValueError:
                print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

        while True:
            while True:
                try:
                    choice = int(menuview.rapport_tournament_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR : ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:

                # 1. Nom et dates du tournoi donné
                case 1:
                    table_to_export, title = tournamentview.display_tournament_name_date(tournament_choice)
                    file_title = f"Details_{title}"
                    menucontroller.launch_export_menu(table_to_export, file_title)
                # 2. Liste des joueurs du tournoi par ordre alphabétique
                case 2:
                    table_to_export, title = tournamentview.display_tournament_players_list(tournament_choice)
                    file_title = f"Joueurs_{title}"
                    menucontroller.launch_export_menu(table_to_export, file_title)
                # 3. Liste de tous les tours du tournoi et de tous les matchs du tour
                case 3:
                    table_to_export, title = tournamentview.display_tournament_rounds(tournament_choice)
                    file_title = f"Tours_{title}"
                    menucontroller.launch_export_menu(table_to_export, file_title)
                # 4. Retour
                case 4:
                    menucontroller.launch_rapport_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 4")

    def launch_export_menu(self, table_to_export, title):
        tournamentview = TournamentView()
        menuview = MenuView()
        while True:
            while True:
                try:
                    choice = int(menuview.export_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:

                # Yes
                case 1:
                    tournamentview.export(table_to_export, title)
                    break
                # No
                case 2:
                    break
                case _:
                    print("[red]ERREUR: Merci d'entrer une valeur de 1 ou 2.[/red]")

    def launch_change_round_menu(self, tournament):
        tournamentview = TournamentView()
        tournamentcontroller = TournamentController()
        menuview = MenuView()
        while True:
            while True:
                try:
                    choice = int(menuview.change_round_number_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

            match choice:

                # Yes
                case 1:
                    round_number = tournamentview.input_round_number(tournament)
                    tournamentcontroller.change_round_number(tournament, round_number)
                    break
                # No
                case 2:
                    break
                case _:
                    print("[red]ERREUR: Merci d'entrer une valeur de 1 ou 2.[/red]")
