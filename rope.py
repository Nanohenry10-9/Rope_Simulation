from time import sleep
from graphics import *
from math import sqrt
win = GraphWin("Rope Physics", 800, 800)

CONST_GRAV = 0.05

class RopeElement():
        def __init__(self, x, y, c1, c2, fixed, objects):
                self.x = x
                self.y = y
                self.sX = 0
                self.sY = 0
                self.f = c1
                self.b = c2
                self.prev = None
                self.fix = fixed
                self.o = objects
                
        def sim(self, coll, index):
                if not self.fix:
                        if not coll:
                                self.mov()
                        else:
                                self.sY = self.sY + CONST_GRAV
                                if self.y > 798:
                                        self.y = 798
                                        self.sY = self.sY * -0.999
                                if self.f != None and sqrt(pow(abs(self.x - self.f.x), 2) + pow(abs(self.y - self.f.y), 2)) > 6:
                                        #self.x = self.x - self.sX
                                        #self.y = self.y - self.sY
                                        newX = (((self.f.x - self.x) / 8) + self.sX)
                                        newY = (((self.f.y - self.y) / 8) + self.sY)
                                        self.sX = newX
                                        self.sY = newY
                                if self.b != None and sqrt(pow(abs(self.x - self.b.x), 2) + pow(abs(self.y - self.b.y), 2)) > 6:
                                        #self.x = self.x - self.sX
                                        #self.y = self.y - self.sY
                                        newX = (((self.b.x - self.x) / 8) + self.sX)
                                        newY = (((self.b.y - self.y) / 8) + self.sY)
                                        self.sX = newX
                                        self.sY = newY
                                for i in range(len(objects)):
                                        if self.x < objects[i].x + objects[i].w and self.x > objects[i].x - objects[i].w and self.y < objects[i].y + objects[i].w and self.y > objects[i].y - objects[i].w:
                                                self.sX = (self.x - objects[i].x) / objects[i].w
                                                self.sY = (self.y - objects[i].y) / objects[i].w
                        if index == 0:
                                pt = win.checkMouse()
                                if pt != None:
                                        newX = (((int(pt.getX()) - self.x) / 50) + self.sX)
                                        newY = (((int(pt.getY()) - self.y) / 50) + self.sY)
                                        self.sX = newX
                                        self.sY = newY

        def mov(self):
                self.x = self.x + self.sX
                self.y = self.y + self.sY
                                        
        def draw(self, i, max):
                if i != max:
                        if self.prev != None:
                                self.prev.undraw()
                        l = Line(Point(self.x, self.y), Point(self.b.x, self.b.y))
                        l.setFill('black')
                        l.setWidth(6)
                        l.draw(win)
                        self.prev = l

        def setConn(self, c1, c2):
                self.f = c1
                self.b = c2

        def setFixed(self, fixed):
                self.fix = fixed

class Object:
        def __init__(self, x, y, w):
                self.x = x
                self.y = y
                self.w = w

        def draw(self):
                c = Circle(Point(self.x, self.y), self.w)
                c.setFill('red')
                c.draw(win)
                

rope = []
ELEMENTS = 40

objects = []

b = Object(325, 500, 40)
b.draw()
objects.append(b)

b = Object(425, 500, 40)
b.draw()
objects.append(b)

b = Object(375, 600, 40)
b.draw()
objects.append(b)


for i in range(ELEMENTS):
        newRope = RopeElement(450 - (ELEMENTS - i) * 4, 90, None, None, False, objects)
        rope.append(newRope)

for i in range(len(rope)):
        if i == 0:
                rope[i].setConn(None, rope[i + 1])
        elif i == len(rope) - 1:
                rope[i].setConn(rope[i - 1], None)
        else:
                rope[i].setConn(rope[i - 1], rope[i + 1])

#rope[len(rope) - 1].setFixed(True) # End fixed
#rope[int(len(rope) / 2)].setFixed(True) # Middle fixed

while True:
        for i in range(len(rope)):
                rope[i].sim(0, i)
        for i in range(len(rope)):
                rope[i].sim(1, i)
                rope[i].draw(i, len(rope) - 1)
        #sleep(0.01)
                
