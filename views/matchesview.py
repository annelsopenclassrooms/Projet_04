from models.tournament import Tournament

class MatchesView:
    
    # enter all matches resultat from a round
    def input_results(self, tournament):
        #get matches from the current round
        print (f"round en cours: {tournament.current_round}")
        matches = tournament.rounds[tournament.current_round].matches
        for match in matches:
            #print(matches)
            print ("Qui a gagné le match?")
            print (f"1. {match[0][0].last_name} {match[0][0].first_name}")
            print (f"2. {match[1][0].last_name} {match[1][0].first_name}")
            print (f"3. Egalité")

            choice = input("choix ?:")
            choice = int(choice)
                        
            match choice:
                case 1:

                    match[0][1] = 1
                    
                    match[0][0].total_points = match[0][0].total_points + 1

                case 2:
                    match[1][1] = 1
                    match[1][0].total_points = match[1][0].total_points + 1


                case 3:
                    match[0][1] = 0.5
                    match[1][1] = 0.5
                    match[0][0].total_points = match[0][0].total_points + 0.5
                    match[1][0].total_points = match[1][0].total_points + 0.5
