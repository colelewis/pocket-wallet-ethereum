import utility
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askdirectory

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("pocket-eth-wallet")
        self.geometry('300x300')

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

        # self.labelA = ttk.Label(self, text = "Start!")
        # self.labelA.grid(column=1, row=1)
        if (utility.any_wallets() == True or True ): #or True condition used for testing
            #choose wallet from directory
            path = askdirectory(title="Choose wallet directory...")
            print(path)
            #button = ttk.Button(self, text="Select wallet directory", command=select_file).pack()
        else:
            #create wallet
            pass

        #create wallet   

class SendTab(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        # self.labelB = ttk.Label(self, text = "Send!")
        # self.labelB.grid(column=1, row=1)
        # send transactions
        # choose address with according balance

class ReceiveTab(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "Receive!")
        self.labelB.grid(column=1, row=1)

if __name__ == '__main__':
    app = GUI()
    app.mainloop()