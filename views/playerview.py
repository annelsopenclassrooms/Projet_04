from controllers.inputcontroller import InputController


class PlayerView:
    def get_player_input(self):
        dict_infos = {}
        
        while True:
            last_name = input("Nom de famille du joueur? : ")
            if InputController.is_last_name(last_name):
                break
            else:
                print("Merci de donner un nom de famille valide")
        dict_infos["last_name"] = last_name

        while True:
            first_name = input("Prénom du joueur? : ")
            if InputController.is_first_name(first_name):
                break
            else:
                print("Merci de donner un prénom valide")

        dict_infos["first_name"] = first_name

        while True:
            birth_date = input("Date de naissance du joueur? : ")
            if InputController.is_birth_date(birth_date):
                break
            else:
                print("Merci de donner une date valide et pas dans le futur")
        dict_infos["birth_date"] = birth_date

        while True:
            chess_id = input("Identifiant du joueur? : ")
            if InputController.is_chess_id(chess_id):
                break
            else:
                print("Merci de donner un identifiant et pas dans le futur")
      
        dict_infos["chess_id"] = chess_id
        

        return (dict_infos)
