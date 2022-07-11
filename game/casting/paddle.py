import pyray
from game.casting.actor import Actor
from game.shared.color import Color


class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self.posX = 30
        self.posY = 30
        self.width = 15
        self.height = 50
        self.color = Color(255, 255, 255)
        self.draw_rec()

    def draw_rec(self):
        pyray.draw_rectangle(self.posX, self.posY, self.width, self.height, self.color)