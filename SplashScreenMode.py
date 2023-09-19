from cmu_112_graphics import *
from DrawFunctions import *
from helpMode import *

'''
This file handles the splash screen that is shown before the game starts. Course
length is entered here and then the game can be started.
'''

def splashScreenMode_redrawAll(app, canvas):
    drawLand(app, canvas)
    drawSky(app, canvas)
    drawPolePositionLogo(app, canvas)
    draw112(app, canvas)
    drawHelpPrompt(app, canvas)
    app.startButton.drawButton(canvas)

def splashScreenMode_mouseMoved(app, event):
    app.startButton.mouseMoved(event)

def splashScreenMode_mousePressed(app, event):
    if app.startButton.inButton(event.x, event.y):
        if app.startButton.text == "SETUP":
            userInput = app.getUserInput("Enter Course Length\n(Must Be > 100)")
            if userInput != None and userInput.isdigit() and int(userInput) > 100:
                app.courseLength = int(userInput)
                app.startButton.text = "RACE"
        elif app.startButton.text == "RACE":
            app.mode = "gameMode"

def splashScreenMode_keyPressed(app, event):
    if event.key == "h":
        app.mode = "helpMode"

def splashScreenMode_sizeChanged(app):
    app.startButton.cx = app.width / 2 
    app.startButton.cy = app.height / 2 + 100