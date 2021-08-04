import numpy as np
import pandas as pd
import tkinter as tk
from tool import Tool


TITLE = "Lapwing Data Tool"
RESOLUTION = "1280x720"
vFRAME_relW = 0.8


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(RESOLUTION)

        self._mFrame = tk.Frame(self, bg='red')  # TODO: remove bg colours after testing
        self._vFrame = tk.Frame(self, bg='green')

        self._mFrame.place(anchor=tk.SE, relx=1, rely=1, relheight=1, relwidth=1 - vFRAME_relW)
        self._vFrame.place(anchor=tk.NW, relx=0, rely=0, relheight=1, relwidth=vFRAME_relW)

        self._df = Tool.get_data("arty-primary.csv")
        self.temp()

    def temp(self):
        print(self._df.to_string())

    def init_rocket(self):
        pass

    def init_menu(self):
        pass

    def plot(self):
        pass
