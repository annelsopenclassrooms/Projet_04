from datetime import datetime
import random
from models.player import Player
from models.tournament import Tournament


class Round:
    all = []

    def __init__(self, name):
        self.name = name
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
        start_time_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time_str = (
            self.end_time.strftime("%Y-%m-%d %H:%M:%S") if isinstance(self.end_time, datetime) else str(self.end_time)
        )
        return (
            f"Round(name='{self.name}', "
            f"start_time='{start_time_str}', "
            f"end_time='{end_time_str}', "
            f"matches={self.matches})"
        )

    def generate_round_matches(self, tournament):

        players = tournament.players

        # TODO if 1er round shuffle et pas de verif paire deja existante

        if tournament.current_round == 0:

            random.shuffle(players)

        else:
            pass

        nb_player = len(players)

        nb_matches = nb_player / 2
        index_player1 = 0
        index_player2 = 1

        #print(tournament.rounds)
        while nb_matches > 0:

            match = ([players[index_player1], 0], [players[index_player2], 0])
            
            if tournament.current_round > 0:
                print(Round.is_existing_pair(players[index_player1], players[index_player2], tournament))
            self.matches.append(match)


            nb_matches = nb_matches - 1
            index_player1 = index_player1 + 2
            index_player2 = index_player2 + 2

    

    @staticmethod
    def is_existing_pair(player1, player2, tournament):
        for round in tournament.rounds:

            for pair in round.matches:

                if (player1 == pair[0][0] and player2 == pair[1][0]) or (player2 == pair[0][0] and player1 == pair[1][0]):
                    return True
                
        return False

