import pyray

from game.casting.actor import Actor
from game.shared.color import Color


class Line(Actor):
    def __init__(self):
        super().__init__()
        self.startPosX = 200
        self.startPosY = 200
        self.endPosX = 100
        self.endPosY = 100
        self.color = Color(255, 255, 255)
        self.draw_line()
        
    def draw_line(self):
        pyray.draw_line(self.startPosX, self.startPosY, self.endPosX, self.endPosY, self.color)

    
        