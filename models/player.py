class Player:

    def __init__(self, last_name, first_name, birth_date, chess_id, total_points: float = 0.0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.total_points = total_points

    def __repr__(self):
        return (f"Player(last_name={self.last_name}, first_name={self.first_name}, "
                f"birth_date={self.birth_date}, chess_id={self.chess_id}, "
                f"total_points={self.total_points})")

    def get_total_points(self):
        print(f"Le joueur {self.last_name} {self.first_name} a {self.total_points} points")

    @staticmethod
    def sort_by_total_points(tournament):

        players = tournament.players

        sorted_players = sorted(players, key=lambda player: player.total_points, reverse=True)
        tournament.players = sorted_players
