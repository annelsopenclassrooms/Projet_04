from models.tounament import Tournament


class TournamentView:
    def get_tournament_input_creation(self):
        dict_tournament_for_json = {}
        dict_tournament_for_json["name"] = input("Nom du tounois ?: ")
        dict_tournament_for_json["location"] = input("Lieu du tounois ?: ")
        dict_tournament_for_json["start_date"] = input("Date de début ?: ")
        dict_tournament_for_json["rounds_number"] = input("Nombre de tours ?: ")
        return (dict_tournament_for_json)

    def add_player_to_tournament(self, id_chess):
        pass

    def display_tournament_infos(self):
        
        print(Tournament.all)


# class TournamentView {
#     +display_tournament_form()
#     +display_tournament_list()
#     +display_tournament_details()
#     +get_tournament_input()
# }

        # self.end_date = end_date
        # self.rounds_number = rounds_number
        # self.current_round = current_round
        # self.rounds = rounds
        # self.players = players
        # self.description = description
