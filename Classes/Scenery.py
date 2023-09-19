from cmu_112_graphics import *
from Helper import *

'''
This file outlines scenery objects like the clouds and hills.
'''

class Scenery:
    sceneryList = []

    def __init__(self, app, cy, sprite, perspective):
        self.sprite = sprite
        self.cx = app.width / 2
        self.cy = cy
        self.offset = 0
        self.perspective = perspective # lower means the object is further away and will move slower
        Scenery.sceneryList.append(self)

    def updateOffset(self, app):
        self.offset += app.curve.curveIntensity * app.curve.curveDirection * self.perspective
    
    def drawScenery(self, app, canvas):
        canvas.create_image(self.cx + self.offset, self.cy, image=ImageTk.PhotoImage(self.sprite), anchor = "s")

    @classmethod
    def updateAllOffsets(cls, app):
        for scenery in Scenery.sceneryList:
            scenery.updateOffset(app)

    @classmethod
    def drawAllScenery(cls, app, canvas):
        for scenery in Scenery.sceneryList:
            scenery.drawScenery(app, canvas)