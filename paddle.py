import pyray

from constants import WHITE


class Paddle:
    def __init__(self, posX, posY, width, height, color):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = color
        self.draw_rectangle()
        
    def draw_rectangle(self):
        pyray.draw_rectangle (self.posX, self.posY, self.width, self.height, self.color)

# Object
paddle1 = Paddle(posX= 20, posY= 20, width= 15, height=15, color= WHITE)
paddle2 = Paddle(posX= -20, posY= -20, width= 15, height=15, color= WHITE)
