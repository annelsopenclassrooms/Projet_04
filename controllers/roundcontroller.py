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

            players_left = []
            for player in players:
                players_left.append(player)

            while True:

                roundcontroller = RoundController()
                player1 = players_left[0]

                # index_player2 = 1 because player_left[0] is player one
                index_player2 = 1
                index_same_total = 0
                index_no_same_total = 0
                nb_shuffle = 0
                nb_shuffle_no_same_total = 0

                # Player with the same total point
                same_total = [player for player in players_left if player.total_points == players_left[0].total_points]
                # Remove player 1 from same total list
                same_total.remove(players_left[0])

                while True:

                    # if there is no other player with same points
                    if len(same_total) == 0:

                        if len(players_left) == 2:
                            player2 = players_left[1]
                            players_left.remove(player1)
                            players_left.remove(player2)
                            match = ([player1, 0], [player2, 0])
                            round.matches.append(match)
                            break

                        if index_no_same_total == len(players_left):

                            player2 = players_left[1]
                            index_no_same_total = index_no_same_total + 1

                        else:

                            if nb_shuffle_no_same_total > len(players_left):
                                player2 = players_left[index_player2]
                                index_player2 = index_player2 + 1
                                nb_shuffle_no_same_total = nb_shuffle_no_same_total + 1

                            else:

                                no_same_total = [player for player in players_left]
                                no_same_total.remove(no_same_total[0])
                                random.shuffle(no_same_total)
                                player2 = no_same_total[0]
                                nb_shuffle_no_same_total = nb_shuffle_no_same_total + 1

                    # if there more than one player with same points
                    if len(same_total) >= 1:

                        if len(players_left) == 2:
                            player2 = players_left[1]
                            players_left.remove(player1)
                            players_left.remove(player2)
                            match = ([player1, 0], [player2, 0])
                            round.matches.append(match)
                            break

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

                            if len(same_total) < nb_shuffle:
                                player2 = players_left[index_player2]
                                index_player2 = index_player2 + 1

                            else:

                                random.shuffle(same_total)
                                player2 = same_total[0]

                                nb_shuffle = nb_shuffle + 1

                    if roundcontroller.is_existing_pair(player1, player2, tournament):
                        pass

                    else:

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

                        # New empty list of match
                        round.matches = []

                        # New list of players
                        for player in players:
                            players_left.append(player)

                        # new indexes
                        index_player2 = 1
                        index_same_total = 0
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

        for round in tournament.rounds:

            for pair in round.matches:
                # if (player1 == pair[0][0] and player2 == pair[1][0]) or
                # (player2 == pair[0][0] and player1 == pair[1][0]):
                if {player1, player2} == {pair[0][0], pair[1][0]}:

                    return True

        return False
