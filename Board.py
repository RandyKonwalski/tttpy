import tkinter as tk
from Field import Status, Field

class Board(tk.Canvas):
    def __init__(self, master=None, cnf={} ,**kw):
        self.sizex = kw.get('width')
        self.sizey = kw.get('height')
        self.fieldsx = kw.get('fieldsx')
        self.fieldsy = kw.get('fieldsy')
        self.padding = 20
        self.objects = []
        self.fields = []
        kw.__delitem__('fieldsx')
        kw.__delitem__('fieldsy')
        super().__init__(master, cnf, **kw)

    def getField(self, id):
        row = id / self.fieldsx
        fid = id - (self.fieldsx * row)
        return self.fields[row][fid]


    def generateFields(self):
        y = 0
        x = 0
        while(y < self.sizey):
            row = []
            while(x < self.sizex):
                row.append(Field(x, y, self.sizex / self.fieldsx, self.sizey / self.fieldsy, self))
                x += self.sizex / self.fieldsx
            self.fields.append(row)
            y += self.sizey / self.fieldsy
            x = 0

    def draw(self):
        for row in self.fields:
            for field in row:
                rect = self.create_rectangle(field.x, field.y, field.x + field.sizex, field.y + field.sizey, outline="#000", fill="#fff")
                self.tag_bind(rect, '<ButtonPress-1>', field.onObjectClick)
                if field.status == Status.CIRCLE:
                    self.objects.append(self.create_oval(field.x + field.padding, field.y + field.padding, field.x + field.sizex - field.padding, field.y + field.sizey - field.padding))
                elif field.status == Status.CROSS:
                    self.objects.append(self.create_line(field.x + field.padding, field.y + field.padding, field.x + field.sizex - field.padding, field.y + field.sizey - field.padding))
                    self.objects.append(self.create_line(field.x + field.padding, field.y + field.sizey - field.padding, field.x + field.sizex - field.padding, field.y + field.padding))

    def redraw(self):
        for obj in self.objects:
            self.delete(obj)
        self.draw()
        self.update()
      
    def checkWinRow(self, row, side):
        if self.fields[row][0] == side and self.fields[row][1] == side and self.fields[row][2] == side:
            return True
        return False

    def checkWinColumn(self, column, side):
        if self.fields[0][column] == side and self.fields[1][column] == side and self.fields[2][column] == side:
            return True
        return False


    def checkWin(self, side):
        if self.fields[0][0].status == side and self.fields[1][1].status == side and self.fields[2][2].status == side:
            return True
        
        if self.fields[0][2].status == side and self.fields[1][1].status == side and self.fields[2][0].status == side:
            return True
        
        if self.checkWinRow(0, side) or self.checkWinRow(1, side) or self.checkWinRow(2, side):
            return True
        
        if self.checkWinColumn(0, side) or self.checkWinColumn(1, side) or self.checkWinColumn(2, side):
            return True

        return False