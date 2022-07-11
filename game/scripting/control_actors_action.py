import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("player_1_scores")
        score2 = cast.get_first_actor("player_2_scores")

        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            score1.add_points(100, "player_1")

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            score1.add_points(100, "player_1")

        snake = cast.get_first_actor("player_1")
        snake.turn_head(self._direction)

        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
            score2.add_points(100, "player_2")

        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            score2.add_points(100, "player_2")

        cycle = cast.get_first_actor("player_2")
        cycle.turn_head(self._direction2)