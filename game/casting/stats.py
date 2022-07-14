from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._score2 = 0
        self._score1 = 0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        if points == 1:
            self._score1 += 1
        else:
            self._score2 += 1

    def get_score2(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._score1

  
    def get_score1(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score2

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score1 = 0
        self._score2 = 0