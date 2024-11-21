"""Entry point."""
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from views.menu import Menu

menu = Menu()
choice = menu.main_menu()

# print("1. Creer des joueurs")
# print("2. Tournois")
# print("3. Rapports")
# print("4. Quitter le programme")

while True:
    
    match choice:
        case 1:
            menu.add_player_choice_list()
            break
        case 2:
            tournament = menu.tournament_menu()
            break
        case 3:
            pass
        case 4:
            exit()

print (tournament)

choice = menu.add_player_choice_list()
player_in_tournament = []
while True:
    choice = menu.add_player_choice_list()
    match choice:
        case 1:
            print("Ajouter un joueur depuis la liste des joueurs existants.")
            player_in_tournament.append(menu.get_player_from_list())
        case 2:
            print("Ajouter un joueur depuis son Chess ID.")
            player_in_tournament.append(menu.get_player_from_chess_id())
        case 3:
            print("Créer un nouveau joueur et l'ajouter au tournoi.")
            playercontroller = PlayerController()
            player_in_tournament.append(playercontroller.create_player())
        case 4:
            print("Fin d'import des joueurs.")
            tournamentcontroller = TournamentController()
            tournamentcontroller.instantiate_players(player_in_tournament, tournament)
            menu.tournament_menu()
            break
        case _:
            print("Choix invalide. Veuillez choisir une option entre 1 et 4.")