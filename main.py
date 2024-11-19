#TODO corrections: blinder tous les input
# empecher 2 fois le meme joueurs dans un tournois
# empecher creation d'un tournois quand un est en cours
#empecher ajout de joueur si tournois pas creer



#TODO features
# matches
# rounds
 
"""Entry point."""

# from models.player import Player
# from views.createplayerview import CreatePlayerView
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu
# c = CreatePlayerView()
# print (c.input_player_info())

# p = PlayerController()
# p.create_player()

# t = TournamentController()
# t.create_tournament()

# p = PlayerController()
# p.get_players_list()

m = Menu()
#m.add_player_choice_list()
m.main_menu()