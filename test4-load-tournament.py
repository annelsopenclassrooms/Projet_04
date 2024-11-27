from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu
from views.tournamentview import TournamentView
from controllers.menucontroller import MenuController
from models.tournament import Tournament
from models.player import Player

if __name__ == "__main__":

    tournamentcontroller = TournamentController()
    tournamentcontroller.load_tournament()
