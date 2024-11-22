"""Entry point."""
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu
from views.tournamentview import TournamentView


def launch_main_menu(tournament):
    #print(f"****Tournois de main menu**** {tournament}")
    choice = menu.main_menu()
       
    match choice:
        #1. Creer des joueurs
        case 1:
            playercontroller = PlayerController()
            playercontroller.create_player()
            #menu.add_player_choice_list()
            
        #2. Tournois
        case 2:
            #tournament = menu.tournament_menu()
            tournament = launch_tournament_menu(tournament)
            
        #3. Rapports
        case 3:
            pass
        #4. Quitter le programme
        case 4:
            exit()

    #print (f"fin de main menu {tournament}")
    return(tournament)

def launch_add_player_menu(tournament):
    #print("****launch_add_player_menu****")
    #print(f"Tournois : {tournament}")
    if not tournament:
        print("Merci de crée un tournois avant d'ajouter les joueurs")
    else: 
                   
        player_in_tournament = []
        while True:
            choice = menu.add_player_choice_list()
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
                    launch_tournament_menu(tournament)
                    break
                case _:
                    print("Choix invalide. Veuillez choisir une option entre 1 et 4.")
    return(tournament)

def launch_tournament_menu(tournament):
    #print(f"******launch tournament menu*******{tournament}")
    menu = Menu()
    tournamentcontroller = TournamentController()
    tournamentview = TournamentView()
    choice = menu.tournament_menu()
    match choice:
        case 1:
            tournament = tournamentcontroller.create_tournament()         
            #print (f"retour tournois creation {tournament}")   
        case 2:
            #print("choix 2")
            #menu.add_player_choice_list()
            tournament = launch_add_player_menu(tournament)
        case 3:
            tournament = tournamentcontroller.start_tournament(tournament)
        case 4:
            #print("case: 4 afficher infos tournois")
            tournamentview.display_tournament_infos(tournament)
        case 5:
            menu.main_menu()
    return (tournament)


if __name__ == "__main__":

    tournament = None

    menu = Menu()
    while True:

        #print(f"boucle main {tournament}")
        tournament = launch_main_menu(tournament)
