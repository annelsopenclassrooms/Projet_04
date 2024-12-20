from controllers.menucontroller import MenuController


def splash_screen():
    with open("splash_screen.txt", "r") as file:
        title = file.read()
    return title


if __name__ == "__main__":

    tournament = None

    menucontroller = MenuController()

    print("♜ ♞ ♝ ♛ BIENVENUE♚ ♝ ♞ ♜")
    print(splash_screen())

    tournament = menucontroller.launch_main_menu(tournament)
