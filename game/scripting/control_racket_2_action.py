from constants import *
from game.scripting.action import Action


class ControlRacket2Action(Action):

    def __init__(self, keyboard_service, racket_group):
        self._keyboard_service = keyboard_service
        self._racket_group = racket_group
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(self._racket_group)
        # if self._keyboard_service.is_key_down(UP_1) and self._racket_group == 'rackets1': 
        #     racket.swing_left()
        # elif self._keyboard_service.is_key_down(DOWN_1) and self._racket_group =='rackets1': 
        #     racket.swing_right()  
        if self._keyboard_service.is_key_down(UP_2) and self._racket_group == 'rackets2': 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(DOWN_2) and self._racket_group =='rackets2': 
            racket.swing_right()
        else: 
            racket.stop_moving()        