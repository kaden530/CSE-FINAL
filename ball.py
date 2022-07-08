import pyray

from constants import WHITE


class Ball:
    def __init__(self, centerX, centerY, radius, color):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.color = color
        self.draw_circle()
        
    def draw_circle(self):
        pyray.draw_circle (self.centerX, self.centerY, self.radius, self.color)

# Object
ball = Ball (centerX= 10, centerY= 10, radius= 10, color= WHITE)
print(ball.draw_circle)
