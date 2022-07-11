import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.line import Line
from game.casting.ball import Ball
from game.casting.paddle import Paddle

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player_1", Cycle(100, 300, constants.CYAN))
    cast.add_actor("player_2", Cycle(745, 300, constants.PURPLE))
    cast.add_actor("player_1_scores", Score())
    cast.add_actor("player_2_scores", Score())
    # cast.add_actor("ball", Ball())
    # cast.add_actor("line", Line())
    # cast.add_actor("paddle", Paddle())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    # script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()