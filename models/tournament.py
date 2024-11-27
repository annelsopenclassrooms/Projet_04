class Tournament:
    all = []
    
    def __init__(self, name, location, start_date, end_date, rounds_number=4, current_round=0, rounds=[], players = [], description = ""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.description = description

        Tournament.all.append(self)

    def __repr__(self):
        return (
            f"Tournament(name={self.name!r}, location={self.location!r}, "
            f"start_date={self.start_date!r}, end_date={self.end_date!r}, "
            f"rounds = len({self.rounds}), "
            f"rounds_number={self.rounds_number}, current_round={self.current_round}, "
            f"players={len(self.players)}, description={self.description!r})"
        )

