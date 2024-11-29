class Tournament:

    def __init__(self, name, location, start_date, end_date, rounds_number=4,
                 description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.description = description
        self.current_round = 0
        self.rounds = []
        self.players = []

    def __repr__(self):
        return (
            f"Tournament(name={self.name!r}, location={self.location!r}, "
            f"start_date={self.start_date!r}, end_date={self.end_date!r}, "
            f"rounds = len({self.rounds}), "
            f"rounds_number={self.rounds_number}, current_round={self.current_round}, "
            f"players={len(self.players)}, description={self.description!r})"
        )
