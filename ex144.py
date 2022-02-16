# Project Euler 144 - Investigating multiple reflections of a laser beam, solved in  0.019612 seconds runtime.
# Exercise: https://projecteuler.net/problem=144
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-144

from decimal import *
import math
import timeit
start = timeit.default_timer()
getcontext()

class Point:
    def __init__(self, x,y):
        self.x, self.y = x,y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Line:
    def __init__(self, start,end):
        self.start = start
        self.end = end

        if (self.end.getX()-self.start.getX()==0):
            self.m = float('inf')
        else:
            self.m = Decimal((end.getY()-start.getY())/(end.getX()-start.getX()))
    def getM(self):
        return self.m
    def getEnd(self):
        return self.end
    def getStart(self):
        return self.start
    def getB(self):
        return -Decimal(self.getM())*Decimal(self.getStart().getX())+Decimal(self.getStart().getY())

    def interactionWithLine(self,line):
        #y=m1x+b1 = m2x +b2 -> m1x-m2x=b2-b1 -> x(m1-m2)=b2-b1
        if self.getM() == float('inf') and line.getM() != float('inf'):
            commonX = self.getStart().getX()
            commonY = line.getM()*commonX + line.getB()
        elif self.getM() != float('inf') and line.getM() == float('inf'):
            commonX = line.getStart().getX()
            commonY = self.getM()*commonX + self.getB()
        elif self.getM() != float('inf') and line.getM() != float('inf'):
            commonX = (line.getB()-self.getB())*(self.getM()-line.getM())
            commonY = self.getM()*commonX + self.getB()
        return Point(commonX,commonY)

    def collisionWithEllipse(self):
        #Find x1,x2 in-relation to 4x^2+y^2=100
        a, b, c = (4+(self.getM()**2)), 2*self.getB()*self.getM(), (self.getB()**2)-100
        delta=Decimal(((b**2)-(4*a*c)).sqrt())
        x1,x2 = Decimal(((-b)-delta)/(2*a)), Decimal(((-b) + delta) / (2 * a))
        #Find y1,y2
        y1, y2 = Decimal(Decimal(self.getM()) * x1 + Decimal(self.getB())), Decimal(Decimal(self.getM()) * x2 + Decimal(self.getB()))

        if str(x2)[:10] == str(self.getStart().getX())[:10] or str(x2)[:10] == str(self.getEnd().getX())[:10]:
            return (Point(x1,y1),Point(x2,y2))
        return (Point(x2,y2),Point(x1,y1))


    def reflection_angle(self):
        col = self.collisionWithEllipse()[0]
        x,y = col.getX(), col.getY()
        slope = y/(4*x)
        incidence = Decimal(math.degrees(math.atan(self.getM())))
        reflection = Decimal(Decimal(2*math.degrees(math.atan(slope))) - incidence)
        return reflection

class Line2(Line):
    def __init__(self,start, ang, length):
        self.start = start
        dx = length * math.cos(math.radians(ang))
        dy = length * math.sin(math.radians(ang))
        self.end = Point(start.getX()+Decimal(dx), start.getY()+Decimal(dy))
        self.m = Decimal(math.tan(math.radians(ang)))


def ex144():
    c = 0
    l1 = Line(Point(0.0, 10.1), Point(1.4, -9.6))
    while (True):
        reflection = l1.reflection_angle()
        collision = l1.collisionWithEllipse()[0]
        if c>1 and (collision.getY() > 0 and\
           (collision.getX() > Decimal(-0.01) and collision.getX() < Decimal(0.01))):
            return c
        #If collision was found then the beam hit.
        l1 = Line2(collision, reflection, 100)
        c += 1

print(ex144())
stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
