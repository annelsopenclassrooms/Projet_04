import json
import os
from views.tournamentview import TournamentView
from views.matchesview import MatchesView
from models.tournament import Tournament
from models.round import Round
from models.player import Player
from controllers.roundcontroller import RoundController


class TournamentController:
    def create_tournament(self):
        tournamentview = TournamentView()
        data = tournamentview.get_tournament_input_creation()
        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
        else:
            # Si le fichier n'existe pas, on initialise une liste vide
            tournaments = []

        # Ajoute le nouveau tournois à la liste
        tournaments.append(data)

        # Sauvegarde les données mises à jour dans le fichier JSON
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        tournament = Tournament(data["name"], data["location"], data["start_date"], data["end_date"], data["rounds_number"])

        print("Le tournois a été crée avec succès.")
        print(tournament.name)

        return (tournament)

    def instantiate_players(self, players, tournament):

        # Création des objets et récupération dans une liste
        players_in_tournament = [Player(**data) for data in players]
        tournament.players = players_in_tournament
        return (players_in_tournament)

    def start_tournament(self, tournament):

        #while True:
        #menucontroller = MenuController()
        round = Round(tournament.current_round)
        roundcontroller = RoundController()
        roundcontroller.generate_round_matches(tournament, round)
        # add round to tournament
        tournament.rounds.append(round)
        matchview = MatchesView()
        matchview.input_results(tournament)

        Player.sort_by_total_points(tournament)

        # Update current round in tournament
        tournament.current_round = tournament.current_round + 1
         
        return(tournament)


    def save_tournament(self, tournament):

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                # Load existing data in a list
                tournaments = json.load(f)

        tournaments.pop(len(tournaments) - 1)

        # Prepare rounds to be stored in a list of dictionnaries
        rounds = []
        for round in tournament.rounds:
            round_to_dict = {}
            round_to_dict["name"] = round.name
            round_to_dict["start_time"] = round.start_time
            round_to_dict["end_time"] = round.end_time
            
            #prepare matches to be stored in a list
            matches = []
            for match in round.matches:
                player1_to_dict = {}
                player2_to_dict = {}

                print(match[0][0].last_name)
                player1_to_dict["last_name"] = match[0][0].last_name
                player1_to_dict["first_name"] = match[0][0].first_name
                player1_to_dict["birth_date"] = match[0][0].birth_date
                player1_to_dict["chess_id"] = match[0][0].chess_id
                player1_to_dict["total_points"] = match[0][0].total_points
                player1_to_dict["match_points"] = match[0][1]


                player2_to_dict["last_name"] = match[1][0].last_name
                player2_to_dict["first_name"] = match[1][0].first_name
                player2_to_dict["birth_date"] = match[1][0].birth_date
                player2_to_dict["chess_id"] = match[1][0].chess_id
                player2_to_dict["total_points"] = match[1][0].total_points
                player2_to_dict["match_points"] = match[1][1]
                matches.append([player1_to_dict, player2_to_dict])

            round_to_dict["matches"] = matches
            rounds.append(round_to_dict)
            players = []
            for player in tournament.players:
                player_to_dict = {}
                player_to_dict["last_name"] = player.last_name
                player_to_dict["first_name"] = player.first_name
                player_to_dict["birth_date"] = player.birth_date
                player_to_dict["chess_id"] = player.chess_id
                player_to_dict["total_points"] = player.total_points
                players.append(player_to_dict)

        # Prepare the infos to be stored in a dict
        dict_tournament_for_json = {}
        dict_tournament_for_json["name"] = tournament.name
        dict_tournament_for_json["location"] = tournament.location
        dict_tournament_for_json["start_date"] = tournament.start_date
        dict_tournament_for_json["end_date"] = tournament.end_date
        dict_tournament_for_json["rounds_number"] = tournament.rounds_number
        dict_tournament_for_json["current_round"] = tournament.current_round
        dict_tournament_for_json["rounds"] = rounds
        dict_tournament_for_json["players"] = players
        dict_tournament_for_json["description"] = tournament.description

        # Ajoute le nouveau tournois à la liste
        tournaments.append(dict_tournament_for_json)

        # Save updated date in JSON
        with open(file_path, "w") as f:
            json.dump(tournaments, f, indent=4)  # On utilise indent pour avoir un fichier lisible

        print("Le tournois a été sauvegardé avec succès.")

        return (tournament)

    def load_tournament(self):

        tournamentview = TournamentView()
        tournamentview.list_tournament_from_json()
        


        #recuperer le number choisi dans la liste
        tournament_number = 5

        file_path = "data/tournaments/tournaments.json"

        if os.path.exists(file_path):
            # Si le fichier existe, on le charge
            with open(file_path, "r") as f:
                tournaments = json.load(f)  # Charge les données existantes dans une liste
        else:
            print ("Aucun tournois sauvegardés")
            return(None)

        players_in_tournament = tournaments[tournament_number - 1]['players']
        rounds_in_tournament = tournaments[tournament_number - 1]['rounds']
        
        players = []
        for player in players_in_tournament:
            players.append(Player(player["last_name"], player["first_name"], player["birth_date"], player["chess_id"], player["total_points"]))
            
        rounds = []
        #print(rounds_in_tournament)
        for round in rounds_in_tournament:
            #get matches
            matches = []
            for match in round["matches"]:

                # Trouver tous les objets avec un nom donné
                
                chess_id_player1 = match[0]['chess_id']
                chess_id_player2 = match[1]['chess_id']
                player1 = [player for player in players if player.chess_id == chess_id_player1]
                player2 = [player for player in players if player.chess_id == chess_id_player2]

                #print(player1)

                match_to_add = ((player1, match[0]['match_points']), (player2, match[1]['match_points']))
                matches.append(match_to_add)

            #print(matches)

            round_to_add = Round(round["name"])
            round_to_add.start_time = round["start_time"]
            round_to_add.end_time = round["end_time"]
            round_to_add.matches = round["matches"]

            print (round_to_add)

            rounds.append(round_to_add)
                    #self.name = name
                   # self.start_time = datetime.now().isoformat()
               # self.end_time = 0
                  # self.matches = []
        #print(rounds)


                
               


        #tournament = Tournament(data["name"], data["location"], data["start_date"], data["end_date"], data["rounds_number"])
        #print(players)
        print("Le tournois a été chargé avec succès.")
        #print(tournament)

        #return (tournament)


