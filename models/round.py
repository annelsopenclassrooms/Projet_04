class Round:

    def __init__(self, name):
        self.name = name
        self.start_time = 0
        self.end_time = 0
        self.matches = []

    def __repr__(self):

        return (f"Round(name='{self.name}', start_time={self.start_time}, "
                f"end_time={self.end_time}, matches={self.matches})")
