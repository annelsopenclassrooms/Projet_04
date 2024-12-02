from rich import print


class MatchesView:

    # enter all matches resultat from a round
    def input_results(self):

        while True:
            try:
                choice = int(input("choix ?:"))
                print(f"Merci ! Vous avez entré : {choice}")
                break
            except ValueError:
                print("[red]ERREUR: ce n'est pas un entier valide. Veuillez réessayer.[/red]")

        return (choice)
