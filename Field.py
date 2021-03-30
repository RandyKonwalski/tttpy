class Status:
    CIRCLE = 2
    CROSS = 1
    NONE = 0

    @staticmethod
    def invert(status):
        if status == Status.CIRCLE:
            return Status.CROSS
        elif status == Status.CROSS:
            return Status.CIRCLE
        raise Exception("Bad use of parameter: status")


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
        if self.status == Status.NONE:
            self.setStatus(self.canvas.side)
            if self.canvas.checkWin(self.canvas.side):
                if self.canvas.side == Status.CIRCLE:
                    print("Circle won!")
                elif self.canvas.side == Status.CROSS:
                    print("Cross won!")
            self.canvas.side = Status.invert(self.canvas.side)
            self.canvas.redraw()

    def setStatus(self, status):
        self.status = status
