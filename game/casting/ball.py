import pyray

from game.casting.actor import Actor
from game.shared.color import Color


class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.centerX = 30
        self.centerY = 20
        self.radius = 15
        self.color = Color(255, 255, 255)
        self.draw_circle()
        
    def draw_circle(self):
        pyray.draw_circle (self.centerX, self.centerY, self.radius, self.color)
        





