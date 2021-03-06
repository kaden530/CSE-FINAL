from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT or x >= (FIELD_RIGHT - BALL_WIDTH):

            stats = cast.get_first_actor(STATS_GROUP)
            if x < 50:
                stats.add_points(1)
            else:
                stats.add_points(2)

            
            
            callback.on_next(TRY_AGAIN) 
            

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):

            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)