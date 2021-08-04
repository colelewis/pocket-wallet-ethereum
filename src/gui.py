import utility
import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("pocket-eth-wallet")
        self.geometry('400x400')

        self.notebook = ttk.Notebook(self)

        self.start_tab = StartTab(self.notebook)
        self.send_tab = SendTab(self.notebook)
        self.receive_tab = ReceiveTab(self.notebook)

        self.notebook.add(self.start_tab, text='Start')
        self.notebook.add(self.send_tab, text='Send')
        self.notebook.add(self.receive_tab, text='Receive')

        self.notebook.pack()

class StartTab(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "Start!")
        self.labelA.grid(column=1, row=1)

class Frame1FrameA(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.LabelA = ttk.Label(self, text="LabelA in FrameA in tab Frame1")
        self.LabelA.grid(column=0, row=0)

        self.LabelB = ttk.Label(self, text="LabelB in FrameA in tab Frame1")
        self.LabelB.grid(column=1, row=0)

class SendTab(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "Send!")
        self.labelB.grid(column=1, row=1)

class ReceiveTab(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "Receive!")
        self.labelB.grid(column=1, row=1)

if __name__ == '__main__':
    app = GUI()
    app.mainloop()