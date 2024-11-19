
import random
from models.player import Player

class Round:
    def __init__(self, name, start_time, matches=[], end_time=0):
        self.name = name
        #crée automatiquament
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    @staticmethod
    def round1_matches():
        list_of_player = Player.all
        random.shuffle(list_of_player)
        nb_player = len(list_of_player)
        nb_matches = nb_player / 2
        matches = []
        while nb_matches > 0:
            matches.append(([list_of_player[0], 0], [list_of_player[1], 0]))
            list_of_player.pop(0)
            list_of_player.pop(0)
            nb_matches = nb_matches - 1
        return (matches)

    def generate_round1_matches(self):
        list_of_player = Player.all
        random.shuffle(list_of_player)
        nb_player = len(list_of_player)
        nb_matches = nb_player / 2
        matches = []
        while nb_matches > 0:
            matches.append(([list_of_player[0], 0], [list_of_player[1], 0]))
            list_of_player.pop(0)
            list_of_player.pop(0)
            nb_matches = nb_matches - 1
        return (matches)
