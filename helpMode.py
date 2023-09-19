from cmu_112_graphics import *
from SplashScreenMode import *

'''
This file handles the help screen that can be accessed from the splash screen.
'''

def helpMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fil = "black")
    text = '''
            Control the car using the mouse:\n
            The screen is split into 3 rows:\n
                - Top row is for acceleration\n
                - Middle row is for maintaining speed\n
                - Bottom row is for braking\n
            The screen is also split into columns:\n
                - The further in either direction your mouse\n
                  moves the sharper your turning will be\n
            \n
            Press 'r' while in the game to reset\n
            Press 'p' to pause or unpause the game
           '''
    canvas.create_text(app.width / 2, app.height / 2, text = text, font = "system 14", fill = "white")

def helpMode_keyPressed(app, event):
    if event.key == "h":
        app.mode = "splashScreenMode"