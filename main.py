#!/usr/bin/env python3
import tkinter as tk
from Board import Board
from Field import Status

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.board = Board(self.master, width=500, height=500, fieldsx=3, fieldsy=3, side=Status.CIRCLE)
        self.create_widgets()

    def create_widgets(self):
        self.board.generateFields()
        self.board.draw()
        self.board.pack()

    def refresh(self):
        self.destroy()
        self.__init__()

root = tk.Tk()
root.geometry('800x800')
app = Application(master=root)
app.mainloop()