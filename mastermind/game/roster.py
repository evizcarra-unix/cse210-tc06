class Roster:
    """
    A collection of players. The responsibility of Roster is to keep track of the players.
    """
    def __init__(self):
        """
        The class constructor.

        Args:
            self (Roster): it's essentially an instance of the pertaining class "Roster".
        """
        self.current = -1
        self.players = []

    def add_player(self, player):
        """
        Has the ability of adding player(s) to the roster.

        Args:
            self(Roster): the instance of class object Roster.
            player(Player): the object responsible to adding player.
        """
        if player not in self.players:
            self.players.append(player)
    
    def #TODO:
        #TODO
