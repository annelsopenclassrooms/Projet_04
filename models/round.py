
import random
from models.player import Player

class Round:
    def __init__(self, name, start_time, end_time, matches):
        self.name = name
        #crée automatiquament
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    @staticmethod
    def round1():
        list_of_player = Player.all
        print (list_of_player)
        random.shuffle(list_of_player)
        print (list_of_player)