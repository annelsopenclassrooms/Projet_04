from datetime import datetime
import random
from models.player import Player

class Round:
    all = []
    def __init__(self, name, matches=[], end_time=0):
        self.name = name
        #crée automatiquament
        self.start_time = datetime.now()
        self.end_time = end_time
        self.matches = matches
        Round.all.append(self)

    def __repr__(self):
        """
        Représentation lisible de l'objet Round.

        Returns:
        - str: Informations sur le nom, l'heure de début/fin, et les matchs.
        """
        start_time_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")  # Format lisible
        end_time_str = (
            self.end_time.strftime("%Y-%m-%d %H:%M:%S") if isinstance(self.end_time, datetime) else str(self.end_time)
        )
        return (
            f"Round(name='{self.name}', "
            f"start_time='{start_time_str}', "
            f"end_time='{end_time_str}', "
            f"matches={self.matches})"
        )



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
        
        while nb_matches > 0:
            self.matches.append(([list_of_player[0], 0], [list_of_player[1], 0]))
            list_of_player.pop(0)
            list_of_player.pop(0)
            nb_matches = nb_matches - 1
            #print(f"self matches {self.matches}")
        
