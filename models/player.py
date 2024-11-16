class Player:
    def __init__(self, last_name, first_name, birth_date, chess_id, total_points ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.total_points = total_points

    def get_total_points(self):
        print (f"Le joueur {self.last_name} {self.first_name} a {self.total_points} points")
    def update_points(self):
		    pass


player = Player("anne", "ls", "25/01/1979",12333, 6)


print(player.total_points)
player.get_total_points()
