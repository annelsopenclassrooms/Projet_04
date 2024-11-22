"""Entry point."""
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu

menu = Menu()

while True:

    choice = menu.main_menu()

    # print("1. Creer des joueurs")
    # print("2. Tournois")
    # print("3. Rapports")
    # print("4. Quitter le programme")

    while True:
        
        match choice:
            case 1:
                menu.add_player_choice_list()
                break
            case 2:
                tournament = menu.tournament_menu()
                break
            case 3:
                pass
            case 4:
                exit()

    print (tournament)