import random
from Helper import *

'''
This file outlines curves that appear in the road. Each object in this class is
an individual curve.
'''

# Structure of curves loosely based on https://codeincomplete.com/articles/javascript-racer-v2-curves/
class Curve:
    def __init__(self, app):
        self.maxCurvature = 0.0003
        self.prevCurvature = app.curvature
        # 1: Left, 0: Straight, -1: Right
        self.curveDirections = [1, 0, -1]
        self.curveIntensities = [1, 0.8, 0.6]
        self.curveDirection = random.choice(self.curveDirections)
        self.curveIntensity = random.choice(self.curveIntensities)
        if self.prevCurvature != 0: self.curveDirection = 0 # always puts a straight portion between curved portions
        self.endCurvature = self.curveDirection * self.curveIntensity * self.maxCurvature
        self.curveLength = random.randint(600, 1000)
        if self.curveDirection == 0: self.curveLength /= 5 # shortens the duration of straight portions
        self.progress = 0
        self.distAtStart = app.car.distanceTraveled
        self.distTraveled = app.car.distanceTraveled - self.distAtStart
        self.tempProgress = 0
        self.isDone = False

    def timerFired(self, app):
        self.distTraveled = app.car.distanceTraveled - self.distAtStart
        if self.isDone:
            app.curve = Curve(app)
        else:
            self.curveRoad(app)

    def curveRoad(self, app):
        self.progress = self.distTraveled / self.curveLength
        if self.progress < 0.33: 
            self.intoCurve(app)
        elif self.progress > 0.33 and self.progress < 0.66:
            pass # holding curve
        elif self.progress > 0.66 and self.progress < 1:
            self.outOfCurve(app)
        else:
            self.isDone = True

    def intoCurve(self, app):
        self.tempProgress = self.progress / 0.33
        app.curvature = self.endCurvature * easeOutSine(self.tempProgress)

    def outOfCurve(self, app):
        self.tempProgress = 1 - ((self.progress - 0.66) / 0.33)
        app.curvature = self.endCurvature * easeInSine(self.tempProgress)

    def calcInertia(self, app):
        if self.curveDirection == -1: #right turn
            app.offset += 6 * self.curveIntensity * (app.car.speed / 4) * easeInOutQuad(self.tempProgress)
        elif self.curveDirection == 1: #left turn
            app.offset -= 6 * self.curveIntensity * (app.car.speed / 4) * easeInOutQuad(self.tempProgress)