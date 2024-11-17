#Chaque match consiste en une paire de joueurs.Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune
#contenant deux éléments : un joueur et un score

class Match:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2