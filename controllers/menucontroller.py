
from views.tournamentview import TournamentView
from views.menuview import MenuView
from views.playerview import PlayerView
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController



class MenuController:

    @staticmethod
    def launch_main_menu(tournament):
        menuview = MenuView()
        while True:
            try:
                choice = int(menuview.main_menu())
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
                MenuController.launch_rapport_menu(tournament)
            # 4. Quitter le programme
            case 4:
                exit()
            case _:
                print("Merci d'entre un valeur comprise entre 1 et 4")
        return(tournament)

    @staticmethod
    def launch_add_player_menu(tournament):
        menuview = MenuView()

        if not tournament:
            print("Merci de créer un tournois avant d'ajouter les joueurs")
        else:
            player_in_tournament = []
            while True:

                while True:
                    try:
                        choice = int(menuview.add_player_choice_list())
                        print(f"Merci ! Vous avez entré : {choice}")
                        break
                    except ValueError:
                        print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

                print("match choice")
                match choice:
                    case 1:
                        print("Ajouter un joueur depuis la liste des joueurs existants.")
                        player_in_tournament.append(menuview.get_player_from_list())
                    case 2:
                        print("Ajouter un joueur depuis son Chess ID.")
                        player_in_tournament.append(menuview.get_player_from_chess_id())
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
        menuview = MenuView()
        tournamentcontroller = TournamentController()
        tournamentview = TournamentView()

        while True:
            try:
                choice = int(menuview.tournament_menu())
                print(f"Merci ! Vous avez entré : {choice}")
                break
            except ValueError:
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

        match choice:
            # 1. Charger un tournois    
            case 1:
                tournament = tournamentcontroller.load_tournament()
            # 2. Creer un tournois
            case 2:
                tournament = tournamentcontroller.create_tournament()
            # 3. Ajouter des joueurs au tournois    
            case 3:
                tournament = MenuController.launch_add_player_menu(tournament)
            # 4. Lancer le tournois
            case 4:
                while True:
                    if tournament.current_round + 1 >= tournament.rounds_number:
                        MenuController.launch_end_of_tournament_menu(tournament)
                        MenuController.launch_main_menu(tournament)

                    else: 
                        tournament = tournamentcontroller.start_tournament(tournament)
                        MenuController.launch_next_round_menu(tournament)
            # 5. Afficher les infos du tournois
            case 5:
                tournamentview.display_tournament_infos(tournament)
            
            # 6. Retour
            case 6:
                menuview.main_menu()
            case _:
                print("Merci d'entrer un valeur entre 1 et 6")
        return (tournament)
    
    def launch_next_round_menu(tournament):
        menuview = MenuView()
        tournamentcontroller = TournamentController()
        tournamentview = TournamentView()

        while True:
            print(f"current round: {tournament.current_round}")
            print(f"round number: {tournament.rounds_number}")

            # if tournament.current_round +1 >= tournament.rounds_number:
            #     print("Le tournoi est fini")
            #     return(tournament)

            while True:
                try:
                    choice = int(menuview.next_round_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")
            
            match choice:

                # 1. Passer au tour suivant
                case 1:
                    return (tournament)
                # 2. Sauvegarder le tournois   
                case 2:
                    tournamentcontroller.save_tournament(tournament)
                # 3. Afficher le classement actuel    
                case 3:
                    tournamentview.display_ranking(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 3")

            #return (tournament)
    

    def launch_end_of_tournament_menu(tournament):
        print("XXXXXXXXX FIN DU TOURNOIS XXXXXXXXXXXX")
        tournamentview = TournamentView()
        tournamentview.display_ranking(tournament)
        return(tournament)


    
    def launch_rapport_menu(tournament):
        menuview = MenuView()
        #tournamentcontroller = TournamentController()
        tournamentview = TournamentView()

        while True:
            while True:
                try:
                    choice = int(menuview.rapport_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")
            
            match choice:

                 # 1. Liste de tous les joueurs par ordre alphabétique
                case 1:
                    playerview = PlayerView()
                    playerview.get_players_list()
                # 2. Liste de tous les tournois
                case 2:
                    tournamentview = TournamentView()
                    tournamentview.list_tournament_from_json()
                    
                # 3. Détails d'un tournois
                case 3:
                    tournamentview = TournamentView()
                    tournamentview.list_tournament_from_json()
                    MenuController.launch_rapport_tournament_menu(tournament)
                # 4. Retour
                case 4:
                    MenuController.launch_main_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 3")

            #return (tournament)

    def launch_rapport_tournament_menu(tournament):
        menuview = MenuView()
        tournamentcontroller = TournamentController()
        tournamentview = TournamentView()

        while True:
            try:
                tournament_choice = int(input("Selectionnez un tournois"))
                print(f"Merci ! Vous avez entré : {tournament_choice}")
                break
            except ValueError:
                print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

        while True:
            while True:
                try:
                    choice = int(menuview.rapport_tournament_menu())
                    print(f"Merci ! Vous avez entré : {choice}")
                    break
                except ValueError:
                    print("Erreur : ce n'est pas un entier valide. Veuillez réessayer.")

            match choice:

                 # 1. Nom et dates du tournoi donné
                case 1:
                    pass
                # 2. Liste des joueurs du tournoi par ordre alphabétique   
                case 2:
                    print("case 2 display_tournament_players_list(tournament_choice) ")
                    tournamentview.display_tournament_players_list(tournament_choice)
                    print("menu apres focntion ")
                # 3. Liste de tous les tours du tournoi et de tous les matchs du tour  
                case 3:
                    tournamentview.display_tournament_rounds(tournament_choice)
                # 4. Retour
                case 4:
                    MenuController.launch_rapport_menu(tournament)
                case _:
                    print("Merci d'entrer un valeur entre 1 et 3")