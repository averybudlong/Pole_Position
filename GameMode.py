from cmu_112_graphics import *
from DrawFunctions import *
import Classes
from main import appStarted

'''
This file handles the main game portion of the project. The road, scenery, car,
etc are all updated in this file.
'''

def gameMode_sizeChanged(app):
    app.cellWidth = app.width / app.cols
    app.cellHeight = app.height / app.rows
    app.startLight.cx = app.width / 2
    app.hills.cx = app.width / 2
    app.hills.cy = app.height / 2
    app.clouds.cx = app.width / 2
    app.clouds.cy = app.height / 2 - 150

def gameMode_redrawAll(app, canvas):
    drawSky(app, canvas)
    drawLand(app, canvas)
    Classes.Scenery.drawAllScenery(app, canvas)
    drawSpeed(app, canvas)
    drawTime(app, canvas)
    drawProgress(app, canvas)
    Classes.Road.drawAllRows(app, canvas)
    app.car.drawCar(app, canvas)
    if app.startLight.state < 5: app.startLight.drawStartLight(canvas)
    # ending screen
    if app.gameOver:
        drawGameOver(app, canvas)
        if app.endingTimeVisible:
            drawEndingTime(app, canvas)

def gameMode_keyPressed(app, event):
    if event.key == "p":
        app.stopped = not app.stopped
    elif event.key == "s":
        doStep(app)
    elif event.key == "r":
        appStarted(app)
    elif event.key == "n": # speed up rows for debugging
        app.totalRowCount += 15

def gameMode_mouseMoved(app, event):
    if app.startLight.state < 4 or app.gameOver: # allows the car to move when the light switches to green
        return
    app.car.mouseMoved(app, event)

def gameMode_timerFired(app):
    if app.stopped:
        return
    app.timeElapsed += app.timerDelay
    if app.timeElapsed % 300 == 0:
        app.endingTimeVisible = not app.endingTimeVisible
    doStep(app)
    
def doStep(app):
    if app.gameOver:
        return

    Classes.Road.updateAllMidLines(app)
    # STARTLIGHT
    if app.timeElapsed % 500 == 0 and app.startLight.state < 5:
        app.startLight.switchStates(app)

    # ROAD OFFSET
    app.curve.calcInertia(app)
    app.car.timerFired(app)

    # CHANGING MODELS, ADDING ROWS, MOVING SCENERY
    if app.car.speed > 0:
        # adding new rows faster as speed goes up
        if app.timeSinceNewRow >= 100 - app.car.speed * 30:
            for i in range(2): # you can adjust the number of iterations in this loop to make the road 'faster'
                newRoadRow = Classes.Road(app)
            app.timeSinceNewRow = 0
            # MOVING SCENERY
            if app.curve.curveDirection != 0 and app.curve.progress < 0.80:
                Classes.Scenery.updateAllOffsets(app)
        if app.timeSinceModelChange >= 500 - (app.car.speed**4):
            app.car.alternateModels()
            app.timeSinceModelChange = 0
    
    # CURVING ROAD
    app.curve.timerFired(app)

    # CHECKING IF CAR IS OFF THE ROAD
    app.car.offRoad(app)
    
    app.timeSinceModelChange += app.timerDelay
    if app.raceStarted:
        app.raceTime += app.timerDelay
        app.timeSinceNewRow += app.timerDelay