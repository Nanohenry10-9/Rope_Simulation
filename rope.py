from time import sleep
from graphics import *
win = GraphWin("Rope Physics", 800, 800)

CONST_GRAV = 0.05

class RopeElement():
    def __init__(self, x, y, c1, c2):
        self.x = x
        self.y = y
        self.sX = 0
        self.sY = 0
        self.f = c1
        self.b = c2
        self.prev = None
    def sim(self):
        self.sY = self.sY + CONST_GRAV
        self.x = self.x + self.sX
        self.y = self.y + self.sY
        if self.y > 800 - 1.5:
            self.y = 800 - 1.5
            self.sY = self.sY * -1
    def draw(self):
        if self.prev != None:
            self.prev.undraw()
        p = Circle(Point(self.x, self.y), 3)
        p.setFill('black')
        p.draw(win)
        self.prev = p

rope = RopeElement(50, 50, None, None)

while True:
    rope.sim()
    rope.draw()
    sleep(0.01)
        
