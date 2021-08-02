import matplotlib as mp
import tkinter as tk


TITLE = "Lapwing Data Tool"
RESOLUTION = "1280x720"
vFRAME_relW = 0.6


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(RESOLUTION)

        self._mFrame = tk.Frame(self, bg='red') # TODO: remove bg colours after testing
        self._vFrame = tk.Frame(self, bg='green')

        self._mFrame.place(anchor=tk.SE, relx=1, rely=1, relheight=1, relwidth=1 - vFRAME_relW)
        self._vFrame.place(anchor=tk.NW, relx=0, rely=0, relheight=1, relwidth=vFRAME_relW)

    def init_rocket(self):
        pass

    def init_menu(self):
        pass

    def plot(self):
        pass