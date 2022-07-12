from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacket1Action(Action):

    def __init__(self, physics_service, audio_service, racket_group):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._racket_group = racket_group
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        racket = cast.get_first_actor(self._racket_group)
        
        ball_body = ball.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body, racket_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    