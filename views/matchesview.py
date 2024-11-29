from rich import print

class MatchesView:

    # enter all matches resultat from a round
    def input_results(self, tournament):
        # Get matches from the current round
        print(f"[dark_blue]Tour en cours: [/dark_blue]{tournament.current_round + 1}")
        matches = tournament.rounds[tournament.current_round].matches
        for match in matches:
            print("Qui a gagné le match?")
            print(f"1. {match[0][0].last_name} {match[0][0].first_name}")
            print(f"2. {match[1][0].last_name} {match[1][0].first_name}")
            print("3. Egalité")

            while True:
                while True:
                    try:
                        choice = int(input("choix ?:"))
                        print(f"Merci ! Vous avez entré : {choice}")
                        break
                    except ValueError:
                        print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

                match choice:
                    case 1:
                        match[0][1] = 1
                        match[0][0].total_points = match[0][0].total_points + 1
                        break
                    case 2:
                        match[1][1] = 1
                        match[1][0].total_points = match[1][0].total_points + 1
                        break
                    case 3:
                        match[0][1] = 0.5
                        match[1][1] = 0.5
                        match[0][0].total_points = match[0][0].total_points + 0.5
                        match[1][0].total_points = match[1][0].total_points + 0.5
                        break
                    case _:
                        print("[red]ERREUR: Merci d'entrer un valeur entre 1 et 3[/red]")
