class Round:
    all = []

    def __init__(self, name):
        self.name = name
        self.start_time = 0
        self.end_time = 0
        self.matches = []
        Round.all.append(self)

    def __repr__(self):
        # """
        # Représentation lisible de l'objet Round.

        # Returns:
        # - str: Informations sur le nom, l'heure de début/fin, et les matchs.
        # """
        # start_time_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        # end_time_str = (
        #     self.end_time.strftime("%Y-%m-%d %H:%M:%S") if isinstance(self.end_time, datetime) else str(self.end_time)
        # )
        # return (
        #     f"Round(name='{self.name}', "
        #     f"start_time='{start_time_str}', "
        #     f"end_time='{end_time_str}', "
        #     f"matches={self.matches})"
        # )
        # return(
        # f"Round(name='{self.name}', "
        # f"start_time='{self.start_time}', "
        # f"end_time='{self.end_time}', "
        # f"matches={self.matches})"
        # )

        return (f"Round(name='{self.name}', start_time={self.start_time}, "
                f"end_time={self.end_time}, matches={self.matches})")
