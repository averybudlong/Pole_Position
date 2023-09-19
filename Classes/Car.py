from cmu_112_graphics import *
import Classes

'''
This file outlines the car. The speed, sprite, and steering are all handled here.
'''

class Car:
    def __init__(self, app):
        # SPRITE
        # Sprites taken from https://www.spriters-resource.com/arcade/poleposition/sheet/94319/
        self.spriteSheet = app.scaleImage(app.loadImage("Sprites/Car/carSpriteSheet.png"), 2)
        # location of sprites on sheet, element 0 is straight
        self.spriteLocations = [
            [8, 20, 216, 132], [264, 20, 472, 132], [520, 20, 728, 132],
            [776, 20, 980, 132], [1028, 20, 1244, 132], [1284, 20, 1500, 132],
            [1536, 20, 1760, 132], [1788, 20, 2020, 132], [2040, 20, 2280, 132]
        ]
        self.x = 80
        self.y = 110
        # TURNING
        self.cols = len(self.spriteLocations) * 2
        self.dir = 0
        self.model = self.getModelA(self.dir)
        self.isModelA = True # used to alternate between models to create moving effect
        self.modelGenerator = self.genModels()
        # SPEED
        self.rows = 3
        self.currRow = None
        self.speed = 0
        self.maxSpeed = 4.5
        # DISTANCE
        self.distanceTraveled = 0

    def mouseMoved(self, app, event):
        self.changeSteeringAngle(app, event)
        rowHeight = app.height / self.rows
        self.currRow = int(event.y / rowHeight)

    def changeSpeed(self):
        if self.currRow == 0:
            self.speed += 0.055 * (self.maxSpeed - self.speed) # speed gain per press goes down the closer you get to max speed
        elif self.currRow == 2:
            self.speed -= 0.05
            if self.speed < 0: self.speed = 0
            elif self.speed < 2: self.speed -= 0.1

    def changeSteeringAngle(self, app, event):
        # prevent indexing error by mouse being moved off the canvas
        if event.x >= app.width or event.x <= 0:
            return
        
        col = int(event.x / (app.width / self.cols))
        colsOnEachSide = self.cols // 2
        if col < colsOnEachSide - 1:
            self.dir = colsOnEachSide - 1 - col
        elif col > colsOnEachSide:
            self.dir = colsOnEachSide - col
        else:
            self.dir = 0
        
        # does not use alternateModels() here because everytime the mouse moves
        # the model would change from A to B or B to A which looks weird
        if self.isModelA:
            self.model = self.getModelA(abs(self.dir))
        else:
            self.model = self.getModelB(abs(self.dir))
        
        if self.dir > 0:
            self.model = self.model.transpose(Image.FLIP_LEFT_RIGHT)

    def getModelA(self, index):
        return self.spriteSheet.crop(self.spriteLocations[index])

    def getModelB(self, index):
        # adjusts the y position of the crop to get the alternate model of the car
        location = list(self.spriteLocations[index])
        location[1], location[3] = 152, 264
        return self.spriteSheet.crop(tuple(location))

    def drawCar(self, app, canvas):
        canvas.create_image(app.cellWidth * self.x, app.cellHeight * self.y, image=ImageTk.PhotoImage(self.model), anchor = "s")

    def alternateModels(self):
        self.model = next(self.modelGenerator)
        if self.dir > 0:
            self.model = self.model.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    def genModels(self):
        while True:
            self.isModelA = True
            yield self.getModelA(abs(self.dir))
            self.isModelA = False
            yield self.getModelB(abs(self.dir))

    def turning(self, app):
        app.offset += (4 * self.speed * (self.dir / 2)) / 10

    def updateDistanceTraveled(self):
        self.distanceTraveled += self.speed

    def timerFired(self, app):
        self.updateDistanceTraveled()
        self.turning(app)
        self.changeSpeed()

    def offRoad(self, app):
        roadWidth = (self.y - 20 - app.startRow) * 1.5
        if abs(app.offset) > roadWidth:
            if self.speed > 1:
                self.speed -= 0.01 * abs(app.offset) # speed decreases the further off the track you get