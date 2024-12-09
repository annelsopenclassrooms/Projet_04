import random

from rich import print

from models.player import Player


class RoundController:

    def generate_round_matches(self, tournament, round):

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
                round.matches.append(match)
                nb_matches = nb_matches - 1
                index_player1 = index_player1 + 2
                index_player2 = index_player2 + 2

        # If not the first round
        else:

            Player.sort_by_total_points(tournament)
            players = tournament.players

            print("players au debut")
            print(players)

            players_left = []
            for player in players:
                players_left.append(player)

            while True:

                print("players left boucle principale")
                
                print(players_left)

                roundcontroller = RoundController()
                player1 = players_left[0]
                print(f"player 1: {player1}")

                # index_player2 = 1 because player_left[0] is player one
                index_player2 = 1
                index_same_total = 0
                index_same_total_unique = 0
                index_no_same_total = 0
                nb_shuffle = 0
                nb_shuffle_no_same_total = 0
                
                # Player with the same total point
                same_total = [player for player in players_left if player.total_points == players_left[0].total_points]
                # Remove player 1 from same total list
                same_total.remove(players_left[0])

                while True:

                    print("players left boucle secondaire")
                    print(players_left)
                    print(f"index_player2: {index_player2}")




                    # if there is no other player with same points
                    if len(same_total) == 0:


                        if len(players_left) == 2:
                            print("###NEW PAIR ADDED TWO PLAYERS LEFT")
                            player2 = players_left[1]
                            players_left.remove(player1)
                            players_left.remove(player2)
                            match = ([player1, 0], [player2, 0])
                            round.matches.append(match)
                            break


                        print("if len(same_total) == 0:")

                        # if index no same total + 1 == nb player left
                        if index_no_same_total == len(players_left):
                        #if index_no_same_total + 1 == len(players_left):
                            print("if index_no_same_total + 1 == len(players_left):")
                            player2 = players_left[1]
                            index_no_same_total = index_no_same_total + 1

                        else:
                            print("else if index_no_same_total + 1 == len(players_left):")



                            if nb_shuffle_no_same_total > len(players_left):
                                print("nb_shuffle_no_same_total = 1")
                                print("shuffle max atteint no_same_total")
                                player2 = players_left[index_player2]
                                index_player2 = index_player2 + 1
                                nb_shuffle_no_same_total = nb_shuffle_no_same_total + 1

                            else:

                                print("!!!!!!Shuffle no same total!!!!!!")
                                no_same_total = [player for player in players_left]
                                no_same_total.remove(no_same_total[0])
                                #no_same_total = [player for player in players_left if player.total_points == players_left[1].total_points]
                                #no_same_total.remove(no_same_total[0])
                                random.shuffle(no_same_total)
                                player2 = no_same_total[0]
                                #index_no_same_total = index_no_same_total + 1
                                nb_shuffle_no_same_total = nb_shuffle_no_same_total + 1

                    # if there is one other player with same points
                    # if len(same_total) == 1:

                    #     print("if len(same_total) == 1:")

                    #     print(f"index_same_total_unique: {index_same_total_unique}")

                    #     player2 = players_left[1 + index_same_total_unique]
                    #     print (f"player 2 same total ==1: {player2} ")
                    #     index_same_total_unique = index_same_total_unique + 1

                    # if there more than one player with same points
                    if len(same_total) >= 1:

                        if len(players_left) == 2:
                            print("###NEW PAIR ADDED TWO PLAYERS LEFT")
                            player2 = players_left[1]
                            players_left.remove(player1)
                            players_left.remove(player2)
                            match = ([player1, 0], [player2, 0])
                            round.matches.append(match)
                            break

                        print("if len(same_total) > 1:")

                        print(f"len(same_total): {len(same_total)}")

                        print(f"index_same_total: {index_same_total}")

                        if (len(same_total)) <= (index_player2):

                            # Change total points
                            # If it's no more non existing pairs
                            if (len(same_total)) <= len(same_total) + index_same_total:

                                player2 = players_left[1 + index_same_total]
                                index_same_total = index_same_total + 1

                            else:

                                player2 = players_left[len(same_total) + index_same_total]
                                index_same_total = index_same_total + 1

                        else:

                            print(f"len(same_total): {len(same_total)}")
                            print(f"nb_shuffle: {nb_shuffle}")

                            if len(same_total) < nb_shuffle:
                                print("if len(same_total) > nb_shuffle:")
                                print("shuffle max atteint")
                                player2 = players_left[index_player2]
                                index_player2 = index_player2 + 1

                            else:

                                print("!!!!!!Shuffle!!!!!!")
                                
                                random.shuffle(same_total)
                                player2 = same_total[0]
                                print(player2)
                                nb_shuffle = nb_shuffle + 1

                    if roundcontroller.is_existing_pair(player1, player2, tournament):
                        print("roundcontroller.is_existing_pair")
                        #index_same_total = index_same_total + 1

                    else:

                        print("###NEW PAIR ADDED")
                        players_left.remove(player1)
                        players_left.remove(player2)
                        match = ([player1, 0], [player2, 0])
                        round.matches.append(match)
                        index_player2 = 1

                        break

                # if no players left
                if len(players_left) == 0:

                    # Redraw because if nb player > nb round we don't want 2 same matches
                    if roundcontroller.is_existing_pair(player1, player2, tournament):

                        print("[red] LAST PAIR EXISTING")

                        # New empty list of match
                        round.matches = []

                        # New list of players
                        for player in players:
                            players_left.append(player)

                        # new indexes
                        index_player2 = 1
                        index_same_total = 0
                        index_same_total_unique = 0
                        index_no_same_total = 0
                        nb_shuffle = 0
                        nb_shuffle_no_same_total = 0

                    # draw is complete and there is no same match
                    else:

                        break

        print(f"[cyan]Matchs du tour {int(round.name) + 1}:[/cyan]")
        for match in round.matches:
            print(
                f"[cyan]{match[0][0].first_name} {match[0][0].last_name} VS [/cyan]"
                f"[cyan]{match[1][0].first_name} {match[1][0].last_name}[/cyan]"
                )

    def is_existing_pair(self, player1, player2, tournament):

        print(f"joueurs testés{player1}, {player2}")
        for round in tournament.rounds:

            for pair in round.matches:
                # if (player1 == pair[0][0] and player2 == pair[1][0]) or
                # (player2 == pair[0][0] and player1 == pair[1][0]):
                if {player1, player2} == {pair[0][0], pair[1][0]}:

                    return True

        return False
