from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu
from views.tournamentview import TournamentView
from controllers.menucontroller import MenuController

if __name__ == "__main__":

    tournament = None

    menu = Menu()
    menucontroller = MenuController()
    while True:

        #print(f"boucle main {tournament}")
        tournament = menucontroller.launch_main_menu(tournament)
