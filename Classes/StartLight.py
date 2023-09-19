from cmu_112_graphics import *

'''
This file outlines the start light that appears at the beginning of the game
'''

class StartLight:
    def __init__(self, app):
        self.cx = app.width / 2
        self.cy = 50
        # Sprites taken from https://www.spriters-resource.com/arcade/poleposition/sheet/97926/
        self.path = "Sprites/Stoplights/stoplight0.png"
        self.sprite = app.scaleImage(app.loadImage(self.path), 2)
        self.state = 0

    def drawStartLight(self, canvas):
        canvas.create_image(self.cx, self.cy, image=ImageTk.PhotoImage(self.sprite))

    def switchStates(self, app):
        self.state += 1
        if self.state > 3:
            app.raceStarted = True
        if self.state > 4:
            return
        self.path = self.path[:-5] + str(self.state) + ".png"
        self.sprite = app.scaleImage(app.loadImage(self.path), 2)