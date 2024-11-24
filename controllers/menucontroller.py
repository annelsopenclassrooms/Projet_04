
from views.tournamentview import TournamentView
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu


class MenuController:

    @staticmethod
    def launch_main_menu(tournament):
        menu = Menu()
        while True:
            try:
                choice = int(menu.main_menu())
                print(f"Merci ! Vous avez entré : {choice}")
                break
            except ValueError:
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

        match choice:
            # 1. Creer des joueurs
            case 1:
                playercontroller = PlayerController()
                playercontroller.create_player()
            # 2. Tournois
            case 2:
                tournament = MenuController.launch_tournament_menu(tournament)
            # 3. Rapports
            case 3:
                pass
            # 4. Quitter le programme
            case 4:
                exit()
            case _:
                print("Merci d'entre un valeur comprise entre 1 et 4")
        return(tournament)

    @staticmethod
    def launch_add_player_menu(tournament):
        menu = Menu()

        if not tournament:
            print("Merci de crée un tournois avant d'ajouter les joueurs")
        else:
            player_in_tournament = []
            while True:

                while True:
                    try:
                        choice = int(menu.add_player_choice_list())
                        print(f"Merci ! Vous avez entré : {choice}")
                        break
                    except ValueError:
                        print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

                print("match choice")
                match choice:
                    case 1:
                        print("Ajouter un joueur depuis la liste des joueurs existants.")
                        player_in_tournament.append(menu.get_player_from_list())
                    case 2:
                        print("Ajouter un joueur depuis son Chess ID.")
                        player_in_tournament.append(menu.get_player_from_chess_id())
                    case 3:
                        print("Créer un nouveau joueur et l'ajouter au tournoi.")
                        playercontroller = PlayerController()
                        player_in_tournament.append(playercontroller.create_player())
                    case 4:
                        print("Fin d'import des joueurs.")
                        tournamentcontroller = TournamentController()
                        tournamentcontroller.instantiate_players(player_in_tournament, tournament)
                        MenuController.launch_tournament_menu(tournament)
                        break
                    case _:
                        print("Choix invalide. Veuillez choisir une option entre 1 et 4.")
        return (tournament)

    @staticmethod
    def launch_tournament_menu(tournament):
        menu = Menu()
        tournamentcontroller = TournamentController()
        tournamentview = TournamentView()

        while True:
            try:
                choice = int(menu.tournament_menu())
                print(f"Merci ! Vous avez entré : {choice}")
                break
            except ValueError:
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")
        
        match choice:
            case 1:
                tournament = tournamentcontroller.create_tournament()
            case 2:
                tournament = MenuController.launch_add_player_menu(tournament)
            case 3:
                tournament = tournamentcontroller.start_tournament(tournament)
            case 4:
                tournamentview.display_tournament_infos(tournament)
            case 5:
                menu.main_menu()
            case _:
                print("Merci d'entrer un valeur entre 1 et 5")
        return (tournament)
