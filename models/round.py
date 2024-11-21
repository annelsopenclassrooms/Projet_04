from datetime import datetime
import random
from models.player import Player
from models.tournament import Tournament

class Round:
    all = []
    def __init__(self, name):
        self.name = name
        #crée automatiquament
        self.start_time = datetime.now()
        self.end_time = 0
        self.matches = []
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

    def generate_round1_matches(self):
        #list_of_player = Player.all
        print("generate round1")
        
        list_of_player = Tournament.all[0].players
        #Tournament.all[0].rounds
        random.shuffle(list_of_player)
        nb_player = len(list_of_player)
        nb_matches = nb_player / 2
        
        print(Tournament.all[0])

        player1 = 0
        player2 = 1
        while nb_matches > 0:
             
            self.matches.append(([list_of_player[player1], 0], [list_of_player[player2], 0]))
            #list_of_player.pop(0)
            #list_of_player.pop(0)
            nb_matches = nb_matches - 1
            #print(f"self matches {self.matches}")
            player1 = player1 + 2 
            player2 = player2 + 2
        print(Tournament.all[0])

    def generate_round(self):
        players = Tournament.all[0].players
        #print(Tournament.all[0].rounds)

        nb_player = len(players)
        nb_matches = nb_player / 2
        
        player1 = 0
        player2 = 1
        while nb_matches > 0:
             
            self.matches.append(([players[player1], 0], [players[player2], 0]))
            #list_of_player.pop(0)
            #list_of_player.pop(0)
            nb_matches = nb_matches - 1
            #print(f"self matches {self.matches}")
            player1 = player1 + 2 
            player2 = player2 + 2
        #print(Tournament.all[0].rounds)
        #print(Tournament.all[0])
        #print("fin de round 1 generate")