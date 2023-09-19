from cmu_112_graphics import *
from Helper import *

'''
This file outlines buttons. The start button on the splash screen is setup in a
subclass of Button.
'''

class Button:
    def __init__(self, cx, cy, width, height):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
    
    def getButtonBounds(self):
        x0 = self.cx - self.width / 2
        y0 = self.cy - self.height / 2
        x1 = self.cx + self.width / 2
        y1 = self.cy + self.height / 2
        return (x0, y0, x1, y1)

    def inButton(self, x, y):
        x0, y0, x1, y1 = self.getButtonBounds()
        if (x >= x0 and x <= x1) and (y >= y0 and y <= y1):
            return True
        else:
            return False

class StartButton(Button):
    def __init__(self, cx, cy, width, height, textColor):
        super().__init__(cx, cy, width, height)
        self.textColor = textColor
        self.setColors()
        self.text = "SETUP"
        self.font = "system 40"

    def setColors(self):
        if self.textColor == "black":
            self.buttonColor = "white"
        else:
            self.buttonColor = "black"
    
    def drawButton(self, canvas):
        canvas.create_rectangle(self.getButtonBounds(), fill = self.buttonColor, outline = self.textColor, width = 5)
        canvas.create_text(self.cx, self.cy, text = self.text, fill = self.textColor, font = self.font)

    def mouseMoved(self, event):
        if self.inButton(event.x, event.y):
            self.textColor = "black"
        else:
            self.textColor = "white"
        self.setColors()