from game.secret_code import Secret_Code
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    """
    def __init__(self):
        """
        Class constructor itself.
        Args:
            self(Director): creates an instance of Director.
        """
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        self._move = None
        self._secret_code = Secret_Code()

        def start_game(self):
            """
            Initiates the game through a loop (hopefully) controlling the sequence of play as well.
            """
            pass

        def _prepare_game(self):
            """
            Responsible in preparing the game prior to it being initiated (excluding prior to be opened). This will
            be getting the names of those players and placing them in a roster type format. This is through the use of
            the Roster.py class.
            """
            for p in range(2):
                name - self.console.read(f'Enter a name for player {n + 1}: ')
                player = Player(name)
                self._roster.add_player(player)

        def _#TODO:
            pass

