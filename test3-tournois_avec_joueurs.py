from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu
from views.tournamentview import TournamentView
from controllers.menucontroller import MenuController
from models.tournament import Tournament
from models.player import Player

if __name__ == "__main__":

    tournament = Tournament("YOP", "Lieux", 12/12/2032, "13/12/2032")

    player1 = Player("Vincent", "Vincent", "01/09/2012", "AZ34333")
    player2 = Player("David", "David", "12/12/1986", "AZ344322")
    player3 = Player("Anne", "Anne", "12/12/1979", "AZ1111111")
    player4 = Player("Noémie", "Noémie", "12/12/2023", "BR5672722")
    # player5 = Player("Juliette", "Juliette", "12/12/12", "AZ27632786")
    # player6 = Player("Clémentine", "Clémentine", "12/12/12", "AZ27632786")
    # player7 = Player("Brian", "Brian", "12/12/12", "AZ27632786")
    # player8 = Player("Tali", "Tali", "12/12/12", "AZ27632786")

    tournament.players.append(player1)
    tournament.players.append(player2)
    tournament.players.append(player3)
    tournament.players.append(player4)
    # tournament.players.append(player5)
    # tournament.players.append(player6)
    # tournament.players.append(player7)
    # tournament.players.append(player8)
    


    menu = Menu()
    menucontroller = MenuController()
    while True:

        #print(f"boucle main {tournament}")
        tournament = menucontroller.launch_main_menu(tournament)


