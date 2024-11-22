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
        random.shuffle(players)
        nb_player = len(players)

        nb_matches = nb_player / 2
        player1 = 0
        player2 = 1
        while nb_matches > 0:

            self.matches.append(([players[player1], 0], [players[player2], 0]))
            nb_matches = nb_matches - 1
            player1 = player1 + 2
            player2 = player2 + 2

    # def generate_round_matches(self, tournament):
    #     players = tournament.players
    #     nb_player = len(players)
    #     nb_matches = nb_player / 2
    #     player1 = 0
    #     player2 = 1
    #     while nb_matches > 0:

    #         self.matches.append(([players[player1], 0], [players[player2], 0]))
    #         nb_matches = nb_matches - 1
    #         player1 = player1 + 2
    #         player2 = player2 + 2
