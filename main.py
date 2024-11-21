"""Entry point."""
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu

menu = Menu()
menu.main_menu()