import Classes
from cmu_112_graphics import *

'''
This file sets up the initial objects / variables and the project should be
run from here.
'''

def appStarted(app):
    # MODE
    app.mode = "splashScreenMode"
    # TIME
    app.timerDelay = 25
    app.timeElapsed = 0
    app.timeSinceModelChange = 0
    app.raceTime = 0
    app.timeSinceNewRow = 0
    # GRID
    app.rows = 120
    app.cols = 160
    app.cellWidth = app.width / app.cols
    app.cellHeight = app.height / app.rows
    # CAR
    app.car = Classes.Car(app)
    # ROAD
    app.courseLength = 25 # number of road rows before ending
    app.tempRowCount = 0 
    app.totalRowCount = 0 # number of road rows created
    app.offset = 0
    app.startRow = 57 # road starts slightly above the midpoint (60) so that the road doesn't come to an exact point
    app.curvature = 0
    Classes.Road.initRoad(app)
    app.curve = Classes.Curve(app)
    # STARTLIGHT
    app.startLight = Classes.StartLight(app)
    app.raceStarted = False
    # SCENERY
    Classes.Scenery.sceneryList = []
    # Sprites taken from https://www.spriters-resource.com/genesis_32x_scd/roadrash/sheet/134100/
    hillsSprite = app.loadImage("Sprites/Scenery/hills.png")
    cloudsSprite = app.loadImage("Sprites/Scenery/clouds.png")
    cy = app.height / 2
    perspective = 1
    app.hills = Classes.Scenery(app, cy, hillsSprite, perspective)
    cy = app.height / 2 - 150
    perspective = 0.5
    app.clouds = Classes.Scenery(app, cy, cloudsSprite, perspective)
    # SPLASH SCREEN
    app.startButton = Classes.StartButton(app.width / 2, app.height / 2 + 100, 200, 100, "black")
    app.cmu112 = app.scaleImage(app.loadImage("Sprites/SplashScreen/112.png"), 1)
    # Logo taken from https://www.deviantart.com/ringostarr39/art/Pole-Position-logo-467577386
    app.polePositionLogo = app.loadImage("Sprites/SplashScreen/PolePositionLogo.png")
    # LAND AND SKY
    # Used this tool to get colors: https://www.w3schools.com/colors/colors_picker.asp
    app.skyColors = ["#9999ff", "#8080ff", "#6666ff", "#4d4dff", "#3333ff",
                     "#1a1aff", "#0000ff", "#0000e6", "#0000cc", "#0000b3",
                     "#000099", "#000080", "#000066", "#00004d", "#000033"]

    app.landColors = ["#70db70", "#5cd65c", "#47d147", "#33cc33",
                      "#2eb82e", "#29a329", "#248f24", "#1f7a1f",
                      "#196619", "#145214", "#0f3d0f", "#0a290a"]

    app.stopped = False
    app.gameOver = False
    app.endingTimeVisible = False

# if these imports come before appStarted then appStarted cant be accessed inside of them IDK why
from GameMode import *
from SplashScreenMode import *

if (__name__ == '__main__'):
    runApp(width = 800, height = 600)