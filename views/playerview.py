class PlayerView:
    def get_player_input(self):
        dict_infos = {}
        dict_for_json = {}
        dict_infos["last_name"] = input("Nom du joueur ?: ")
        dict_infos["first_name"] = input("Prénom du joueur ?: ")
        dict_infos["birth_date"] = input("Date de naissance ?: ")
        dict_infos["chess_id"] = input("Identifiant echec ?: ")
        # dict_for_json[chess_id] = dict_infos

        return (dict_infos)
