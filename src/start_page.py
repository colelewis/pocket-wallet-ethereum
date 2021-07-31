import tkinter as tk
from tkinter import ttk

class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.labelA = ttk.Label(self, text = "This is on Frame One")
        self.labelA.grid(column=1, row=1)

        self.frame = Frame1FrameA(self)
        self.frame.grid(row=1, columnspan=2)

class Frame1FrameA(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.LabelA = ttk.Label(self, text="LabelA in FrameA in tab Frame1")
        self.LabelA.grid(column=0, row=0)

        self.LabelB = ttk.Label(self, text="LabelB in FrameA in tab Frame1")
        self.LabelB.grid(column=1, row=0)