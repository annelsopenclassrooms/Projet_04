from controllers.playercontroller import PlayerController
#from controllers.tournamentcontroller import TournamentController
#from views.tournamentview import TournamentView


class Menu:

    def main_menu(self):
        while True:
            print("Menu Principal")
            print("1. Creer des joueurs")
            print("2. Tournois")
            print("3. Rapports")
            print("4. Quitter le programme")
            choice = input("choix ?:")
            
            return (choice)

    def tournament_menu(self):
        #tournamentview = TournamentView()
        #while True:
        print("Menu tournois")
        print("1. Creer un tournois")
        print("2. Ajouter des joueurs au tournois")
        print("3. Lancer le tournois")
        print("4. Afficher les infos du tournois")
        print("5. Retour")
        choice = input("choix ?:")
        return (choice)

    def add_player_choice_list(self):
        # TODO: faire en sorte que player_in_tournament ne soit pas ecraser si on retourne dans le menu
        # verifier avant ajout au dictionnaire que le joueur n'est pas deja dans la liste
        #player_in_tournament = []
        #while True:
            
            #print (player_in_tournament)
        print("Ajouter un joueur au tournois:")
        print("1. Depuis la liste des joueurs existants")
        print("2. Depuis son chess ID")
        print("3. Creer un nouveau joueur et l'ajouter au tournois")
        print("4. Tous les joueurs sont importés")
        choice = input("choix ?:")
        choice = int(choice)
        print(choice)
        #menu = Menu()

        return(choice)
            
  
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
    
    # choice 2
    def get_player_from_chess_id(self):
        chess_id_searched = input("chess id?: ")
        playercontroller = PlayerController()
        result = playercontroller.search_chess_id(chess_id_searched)
        if result:
            return (result)
        else:
            print("joueur non trouvé")

    
    def next_round_menu(self):
        print("Menu tour")
        print("1. Passer au tour suivant")
        print("2. Sauvegarder le tournois")
        print("3. Afficher le classement actuel")

        choice = input("choix ?:")
        return (choice)

