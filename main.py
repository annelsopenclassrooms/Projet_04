from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController

from views.tournamentview import TournamentView
from controllers.menucontroller import MenuController

def splash_screen():
    title=r'''
  _________                           _________ .__                          
 /   _____/__ ________   ___________  \_   ___ \|  |__   ____   ______ ______
 \_____  \|  |  \____ \_/ __ \_  __ \ /    \  \/|  |  \_/ __ \ /  ___//  ___/
 /        \  |  /  |_> >  ___/|  | \/ \     \___|   Y  \  ___/ \___ \ \___ \ 
/_______  /____/|   __/ \___  >__|     \______  /___|  /\___  >____  >____  >
        \/      |__|        \/                \/     \/     \/     \/     \/ 
___________                                                      __          
\__    ___/___  __ _________  ____ _____    _____   ____   _____/  |_        
  |    | /  _ \|  |  \_  __ \/    \\__  \  /     \_/ __ \ /    \   __\       
  |    |(  <_> )  |  /|  | \/   |  \/ __ \|  Y Y  \  ___/|   |  \  |         
  |____| \____/|____/ |__|  |___|  (____  /__|_|  /\___  >___|  /__|         
                                 \/     \/      \/     \/     \/             
   _____                                                                     
  /     \ _____    ____ _____     ____   ___________                         
 /  \ /  \\__  \  /    \\__  \   / ___\_/ __ \_  __ \                        
/    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/                        
\____|__  (____  /___|  (____  /\___  / \___  >__|                           
        \/     \/     \/     \//_____/      \/ 
    '''
    return title

if __name__ == "__main__":

    tournament = None

    #menumenuview = MenuView()
    menucontroller = MenuController()
        #print(f"boucle main {tournament}")
    print ("♜ ♞ ♝ ♛ BIENVENUE♚ ♝ ♞ ♜")
    print (splash_screen())
    tournament = menucontroller.launch_main_menu(tournament)

