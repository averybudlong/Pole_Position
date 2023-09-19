import math

'''
This file contains a few helper functions that are used throughout the project.
'''

# Easing function from https://easings.net/#easeInOutQuad
def easeInOutQuad(progress):
    if progress < 0.5:
        return 2 * progress**2
    else:
        return 1 - (-2 * progress + 2)**2 / 2

# Easing function from https://easings.net/#easeInSine
def easeInSine(progress):
    return 1 - math.cos((progress * math.pi) / 2)

# Easing function from https://easings.net/#easeOutSine
def easeOutSine(progress):
    return math.sin((progress * math.pi) / 2)

# Adapted from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    x0 = col * app.cellWidth
    y0 = row * app.cellHeight
    return (x0, y0, x0 + app.cellWidth, y0 + app.cellHeight)

# Adapted from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCell(app, x, y):
    row = int(y / app.cellHeight)
    col = int(x / app.cellWidth)
    return (row, col)

# https://www.cs.cmu.edu/~112/notes/notes-variables-and-functions.html
def roundHalfUp(d):
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))