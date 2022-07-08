import pyray

from constants import MAX_X, MAX_Y


class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def draw_window(self):
        pyray.init_window(self.width, self.height, self.title)

# Object
window = Window(width= MAX_X, height= MAX_Y, title= 'Pong')
print(window)
