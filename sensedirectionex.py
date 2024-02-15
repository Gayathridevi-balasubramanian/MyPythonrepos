import os
import time
from termcolor import colored
import math


class Canvas():
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [ [' ' for y in range(self._y)] for x in range(self._x) ]

    def setPos(self, pos , mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round( point[1]) < 0 or round(point[1]) >= self._y

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print(self):
        self.clear()
        for y in range(self._y):
            #print ([col[y] for col in self._canvas])
            print(' '.join([col[y] for col in self._canvas]))
         

class TerminalScribe():
    def __init__(self, canvas):
        self.canvas = canvas
        
        self.mark = "*"
        self.trail = "."
        self.pos = [0,0]
        self.direction = [0, 1]
        self.framerate = 0.05
        
    def setdegrees(self, degree):
        radians = (degree/180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]
        
       
    def forward(self):
        pos = [self.pos[0] + self.direction[0] , self.pos[1] + self.direction[0]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
            time.sleep(self.framerate)
        
            
    def draw(self,pos):
        self.canvas.setPos(self.pos ,self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos , self.mark)
        self.canvas.print()
        time.sleep(self.framerate)

    

    def drawslantline(self,degrees):
        self.setdegrees(degrees)
        for i in range(30):
            self.forward()


    def up(self):
        #set the position 
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        #update the pos with its coordinatea
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
   
    def drawsquare(self,side):
        self.side = side
        for i in range(0,self.side):
            self.right()        
        for i  in range(0,self.side):
            self.down()
        for i in range(0, self.side):
            self.left()
        for i in range(0, self.side):
            self.up()
    

c = Canvas(50,50)
ts = TerminalScribe(c)
ts.drawsquare(7)
ts.drawslantline(120)

        