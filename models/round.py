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
        nb_player = len(players)
        nb_matches = nb_player / 2
        index_player1 = 0
        index_player2 = 1

        if tournament.current_round == 0:

            random.shuffle(players)
            
            while nb_matches > 0:
                players = tournament.players
                match = ([players[index_player1], 0], [players[index_player2], 0])
                self.matches.append(match)
                nb_matches = nb_matches - 1
                index_player1 = index_player1 + 2
                index_player2 = index_player2 + 2


        #pas le 1er round
        else:
            Player.sort_by_total_points(tournament)
            players = tournament.players
            players_left = []
            for player in players:
                players_left.append(player)

            wt=0
            while True:
                print(f"round: {tournament.current_round}, while true Principal {wt}, joueurs restant {len(players_left)}")
                wt = wt + 1

                # if len(players_left) == 0:
                #     break

                player1 = players_left[0]
                index_player2 = 0
                index_same_total = 0
                index_no_same_total = 0
                # Player with the same total point
                same_total = [player for player in players_left if player.total_points == players_left[0].total_points]
                same_total.remove(players_left[0])

                wt2 = 0
                while True:
                    print(f"while true secondaire {wt}")
                    
                    if len(same_total) == 0:
                        if len(players_left) == 2:
                            player2 = players_left[1]
                            print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")
                            players_left.remove(player1)
                            players_left.remove(player2)      
                            match = ([player1, 0], [player2, 0])
                            self.matches.append(match)           
                            break           

                        else:
                            if index_no_same_total + 1 == len(players_left):
                                player2 = players_left[1]
                                print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")
                                players_left.remove(player1)
                                players_left.remove(player2)      
                                match = ([player1, 0], [player2, 0])
                                self.matches.append(match)           
                                break    

                            else:
                                print(f"dans len(same total) = 0 et player_left != 2, index_no_same_total + 1: {index_no_same_total + 1}, len(players_left):{len(players_left)}")
                                player2 = players_left[index_no_same_total + 1]
                                print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")
                                index_no_same_total = index_no_same_total + 1
                    if len(same_total) > 0:

                        if (len(same_total)) <= (index_player2):
                            print("changement de total point")
                            #si plus de possibilite sans prendre pair exsitante
                            if (len(same_total)) <=len(same_total) + index_same_total:
                                player2 = players_left[1]
                                print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")
                                players_left.remove(player1)
                                players_left.remove(player2)
                                match = ([player1, 0], [player2, 0])
                                self.matches.append(match)
                                break
                            else:
                                player2 = players_left[len(same_total) + index_same_total]
                                print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")

                        else:
                            print("shuffle")
                            #Shuffle player with same total point
                            random.shuffle(same_total)

                            player2 = same_total[index_player2]
                            print(f"xxxxxxxxxxxxxx player1: {player1.first_name} VS player2: {player2.first_name}")


                    print(f"pair is existing: {Round.is_existing_pair(player1, player2, tournament)}")
                    if Round.is_existing_pair(player1, player2, tournament):

                        index_player2 = index_player2 + 1
                        index_same_total = index_same_total + 1
                    else:
                        players_left.remove(player1)
                        players_left.remove(player2)
                        match = ([player1, 0], [player2, 0])
                        self.matches.append(match)
                        break


                if len(players_left) == 0:
                    print("break")
                    break





            # while nb_matches > 0:
            #     existing_match = True
            #     while existing_match:
            #         players = tournament.players
            #         match = ([players[index_player1], 0], [players[index_player2], 0])
            #         print(Round.is_existing_pair(players[index_player1], players[index_player2], tournament))

            #         self.matches.append(match)

                    
            #         # Index update
            #         index_player1 = index_player1 + 2
            #         index_player2 = index_player2 + 2

            #         nb_matches = nb_matches - 1
            #         existing_match = False
        #print(tournament)

    @staticmethod
    def is_existing_pair(player1, player2, tournament):
        for round in tournament.rounds:

            for pair in round.matches:

                if (player1 == pair[0][0] and player2 == pair[1][0]) or (player2 == pair[0][0] and player1 == pair[1][0]):
                    return True
                
        return False

