class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds_number, current_round, rounds, players, description = ""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.description = description

