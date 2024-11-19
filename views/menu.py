from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.tournamentview import TournamentView


class Menu:

    def main_menu(self):
        while True:
            print("Menu Principal")
            print("1. Creer des joueurs")
            print("2. Tournois")
            print("3. Rapports")
            choice = int(input("choix ?:"))
            m = Menu()

            match choice:
                case 1:
                    pass
                case 2:
                    m.tournament_menu()
                    pass
                    break
                case 3:
                    pass

    def tournament_menu(self):
        tv = TournamentView()
        while True:
            print("Menu tournois")
            print("1. Creer un tournois")
            print("2. Ajouter des joueurs au tournois")
            print("3. Lancer le tournois")
            print("3. Afficher les infos du tournois")
            print("4. Retour")
            choice = int(input("choix ?:"))
            m = Menu()
            tc = TournamentController()
            match choice:
                case 1:
                    tc.create_tournament()            
                case 2:
                    m.add_player_choice_list()
                case 3:
                    pass
                case 4:
                    tv.display_tournament_infos()
                case 4:
                    m.main_menu()



    def add_player_choice_list(self):
        # TODO: faire en sorte que player_in_tournament ne soit pas ecraser si on retourne dans le menu
        # verifier avant ajout au dictionnaire que le joueur n'est pas deja dans la liste
        player_in_tournament = []
        while True:
            
            #print (player_in_tournament)
            print("Ajouter un joueur au tournois:")
            print("1. Depuis la liste des joueurs existants")
            print("2. Depuis son chess ID")
            print("3. Creer un nouveau joueur et l'ajouter au tournois")
            print("4. Tous les joueurs sont importés")
            choice = input("choix ?:")
            choice = int(choice)
            print(choice)
            m = Menu()
            
            match choice:
                case 1:
                    print("Ajouter un joueur depuis la liste des joueurs existants.")
                    player_in_tournament.append(m.get_player_from_list())
                case 2:
                    print("Ajouter un joueur depuis son Chess ID.")
                    player_in_tournament.append(m.get_player_from_chess_id())
                case 3:
                    print("Créer un nouveau joueur et l'ajouter au tournoi.")
                    p = PlayerController()
                    player_in_tournament.append(p.create_player())


                case 4:
                    print("Fin d'import des joueurs.")
                    t = TournamentController()
                    t.instantiate_players(player_in_tournament)
                    # TODO: instancier les joueurs => Fait
                    m.tournament_menu()
                    break
                case _:
                    print("Choix invalide. Veuillez choisir une option entre 1 et 4.")
    
    # choice 1
    def get_player_from_list(self):
        #player_in_tournament = []
        print("liste des joueurs")
        p = PlayerController()
        list = p.get_players_list()
        choice = input("choix ?:")
        choice = int(choice) - 1
        print(list[choice])

        return (list[choice])
    
    def get_player_from_chess_id(self):
        chess_id_searched = input("chess id?: ")
        p = PlayerController()
        result = p.search_chess_id(chess_id_searched)
        if result:
            return (result)
        else:
            print("joueur no trouvé")

