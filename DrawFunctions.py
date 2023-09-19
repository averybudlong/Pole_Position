from cmu_112_graphics import *
from Helper import *

'''
This file contains draw functions that aren't tied to a specific class
'''

def drawGameOver(app, canvas):
    canvas.create_text(app.width / 2, app.height / 2 - 60, text = "GAME OVER",
                    font = "system 50", fill = "red")

def drawEndingTime(app, canvas):
    canvas.create_text(app.width / 2, app.height / 2, text = f"TIME: {(app.raceTime / 1000):.1f}",
                       font = "system 40", fill = "white")

def drawSky(app, canvas):
    skyStart = app.height / 2
    rowHeight = skyStart / len(app.skyColors)
    for i in range(len(app.skyColors)):
        canvas.create_rectangle(0, skyStart - rowHeight * i, app.width, skyStart - rowHeight * (i + 1),
                                fill = app.skyColors[i], width = 0)

def drawLand(app, canvas):
    landEnd = app.height / 2
    rowHeight = landEnd / len(app.landColors)
    for i in range(len(app.landColors)):
        canvas.create_rectangle(0, app.height - rowHeight * i, app.width, app.height - rowHeight * (i + 1),
                                fill = app.landColors[i], width = 0)

def drawSpeed(app, canvas):
    canvas.create_text(5, 20, text = f"SPEED: {(app.car.speed * 40):.1f}", font = "system 18", anchor = "w", fill = "white")

def drawTime(app, canvas):
    canvas.create_text(5, 50, text = f"TIME: {(app.raceTime / 1000):.1f}", font = "system 18", anchor = "w", fill = "white")

def drawProgress(app, canvas):
    # 63 rows spawn at the start so they arent counted towards progress
    # 22.5 is the approx height of the finish line
    progress = ((app.totalRowCount - 63) / (app.courseLength - 22.5)) * 100
    if app.gameOver: progress = 100.0
    canvas.create_text(5, 80, text = f"PROGRESS: {(progress):.1f}%",
                       font = "system 18", anchor = "w", fill = "white")

def drawPolePositionLogo(app, canvas):
    canvas.create_image(app.width / 2, app.height / 2 - 100, image=ImageTk.PhotoImage(app.polePositionLogo))

def draw112(app, canvas):
    canvas.create_image(app.width / 2 - 250, app.height / 2 - 160, image=ImageTk.PhotoImage(app.cmu112))

def drawHelpPrompt(app, canvas):
    canvas.create_text(app.width / 2, app.height - 50, text = "Press 'h' to Toggle Help Menu", font = "system 24", fill = "white")