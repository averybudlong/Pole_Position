from cmu_112_graphics import *
from Helper import *

'''
This file outlines the road. Each object in the Road class is an individual
road row.
'''

# Structure of road loosely based on https://codeincomplete.com/articles/javascript-racer-v2-curves/
class Road:
    roadRows = []

    def __init__(self, app):
        app.totalRowCount += 1
        app.tempRowCount += 1
        # alternating the road color
        if app.tempRowCount > 9: app.tempRowCount = 0
        if app.tempRowCount <= 4: self.roadColor = "#7a7979"
        else: self.roadColor = "#919191"
        # alternating the edge color
        if app.tempRowCount > 8: app.tempRowCount = 0
        if app.tempRowCount <= 3: self.edgeColor = "red"
        else: self.edgeColor = "white"
        # drawing finish line
        if app.totalRowCount >= app.courseLength and app.totalRowCount <= app.courseLength + 10:
            self.roadColor = "#660000"
        if app.totalRowCount >= app.courseLength + 40:
            app.gameOver = True
        self.startRow = app.startRow
        self.row = app.startRow
        self.rowHeight = 1
        self.updateMidLine(app)
        self.updateRoadWidth()
        Road.moveAllRoadRows(app) # moves all existing road rows down to accommodate new row
        Road.updateAllMidLines(app)
        Road.roadRows.append(self)

    def updateMidLine(self, app):
        self.midLine = roundHalfUp(app.curvature * (self.row - 124)**3 + 80 + app.offset)
    
    def updateRoadWidth(self):
        self.roadWidth = roundHalfUp((self.row - self.startRow) * 1.5)

    def moveRoad(self, app):
        self.updateRoadWidth()
        self.row += self.rowHeight
    
    def drawRoad(self, app, canvas):
        x0, y0, x1, y1 = getCellBounds(app, self.row, self.midLine)
        pixRoadWidth = self.roadWidth * app.cellWidth
        canvas.create_rectangle(x0 - pixRoadWidth, y0, x1 + pixRoadWidth, y1, fill = self.roadColor, width = 0) # main body of road

        edgeWidth = (self.row - self.startRow) // 6
        x0, y0, x1, y1 = getCellBounds(app, self.row, self.midLine + self.roadWidth) 
        canvas.create_rectangle(x0 - (edgeWidth * app.cellWidth), y0, x1, y1, fill = self.edgeColor, width = 0) # right edge
        x0, y0, x1, y1 = getCellBounds(app, self.row, self.midLine - self.roadWidth)
        canvas.create_rectangle(x0 - (edgeWidth * app.cellWidth), y0, x1, y1, fill = self.edgeColor, width = 0) # left edge

    @classmethod
    def moveAllRoadRows(cls, app):
        for roadRow in cls.roadRows:
            roadRow.moveRoad(app)
            if roadRow.row > app.rows:
                cls.roadRows.remove(roadRow)
    
    @classmethod
    def drawAllRows(cls, app, canvas):
        for roadRow in cls.roadRows:
            if roadRow.row < (app.rows * 0.50):
                return
            roadRow.drawRoad(app, canvas)

    @classmethod
    def updateAllMidLines(cls, app):
        for roadRow in cls.roadRows:
            roadRow.updateMidLine(app)

    @classmethod
    def initRoad(cls, app): # sets up road prior to start
        Road.roadRows = []
        for i in range(app.rows - app.startRow):
            newRoadRow = Road(app)