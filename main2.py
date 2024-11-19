#from controllers.playercontroller import PlayerController
#from controllers.tournamentcontroller import TournamentController
#from views.menu import Menu
from views.matchesview import MatchesView
import random

from models.round import Round
from models.player import Player
from models.tounament import Tournament

player1 = Player("cathy", "aze", "12/12/12", "aze232323")
player2 = Player("anne", "aze", "12/12/12", "aze232323")
player3 = Player("lucie", "aze", "12/12/12", "aze232323")
player4 = Player("clarisse", "aze", "12/12/12", "aze232323")
#Round.round1_matches()

Tournament("aze", "ezaea", "12", "6")
# print(Tournament.all[0])
# print("#####")
#Tournament.all[0].rounds.append(Round.round1_matches())
#print(Tournament.all[0])
#print("#####")
Tournament.all[0].rounds.append(Round.round1_matches())
#print(Tournament.all[0])
# matches = Tournament.all[0].rounds[Tournament.all[0].current_round]
# print (matches)
m = MatchesView()
m.input_results()