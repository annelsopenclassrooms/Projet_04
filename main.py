"""Entry point."""

# from models.player import Player
# from views.createplayerview import CreatePlayerView
from controllers.playercontroller import PlayerController

# c = CreatePlayerView()
# print (c.input_player_info())

p = PlayerController
p.create_player()
