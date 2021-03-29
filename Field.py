class Status:
    CIRCLE = 2
    CROSS = 1
    NONE = 0

class Field:
    def __init__(self, x, y, sizex, sizey, canvas):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.status = Status.NONE
        self.canvas = canvas
        self.padding = 10

    def onObjectClick(self, event):
        if self.status < 2:
            self.setStatus(self.status + 1)
        else:
            self.setStatus(Status.NONE)
        
        ciw = self.canvas.checkWin(Status.CIRCLE)
        crw = self.canvas.checkWin(Status.CROSS)

        if ciw:
            print("circle won")
        
        if crw:
            print("cross won")
        
        self.canvas.redraw()

    def setStatus(self, status):
        self.status = status
