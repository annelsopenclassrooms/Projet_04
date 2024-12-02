
from rich import print

from views.matchesview import MatchesView


class MatchesController:

    # enter all matches resultat from a round
    def get_results(self, match):
        matchviews = MatchesView()

        print("Qui a gagné le match?")
        print(f"1. {match[0][0].last_name} {match[0][0].first_name}")
        print(f"2. {match[1][0].last_name} {match[1][0].first_name}")
        print("3. Egalité")

        choice = matchviews.input_results()

        while True:
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

        return (match)

    def match_is_played(self, match):
        played = True
        if match[0][1] == 0 and match[1][1] == 0:
            played = False
        return (played)
