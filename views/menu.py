from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController


class Menu:
    def add_player_choice_list(self):
        # TODO: faire en sorte que player_in_tournament ne soit pas ecraser si on retourne dans le menu
        # verifier avant ajout au dictionnaire que le joueur n'est pas deja dans la liste
        player_in_tournament = []
        while True:
            
            #print (player_in_tournament)
            print("Ajouter un joueur:")
            print("1. Depuis la liste des joueurs existants")
            print("2. Depuis son chess ID")
            print("3. Creer un nouveau joueur et l'ajouter au tournois")
            print("4. Tous les joueurs sont importés")
            choice = input("choix ?:")
            choice = int(choice)
            print(choice)
            
            match choice:
                case 1:
                    print("Ajouter un joueur depuis la liste des joueurs existants.")
                    m = Menu()
                    player_in_tournament.append(m.get_player_from_list())
                case 2:
                    print("Ajouter un joueur depuis son Chess ID.")
                    m = Menu()
                    #m.get_player_from_chess_id()
                    player_in_tournament.append(m.get_player_from_chess_id())
                case 3:
                    print("Créer un nouveau joueur et l'ajouter au tournoi.")
                    p = PlayerController()
                    player_in_tournament.append(p.create_player())


                case 4:
                    print("Fin d'import des joueurs.")
                    t = TournamentController()
                    t.instantiate_players(player_in_tournament)
                    # TODO: instancier les joueurs
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

