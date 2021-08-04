import sys
import time
import tkinter as tk
import tkinter.messagebox as alert
import tool as tl


TITLE = "Lapwing Data Tool"
RESOLUTION = "1280x720"
vFRAME_relW = 0.8


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(RESOLUTION)
        self.iconphoto(True, tk.PhotoImage(file="sprites/rocket.png"))

        self._mFrame = tk.Frame(self)
        self._vFrame = tk.Frame(self)

        self._mFrame.place(anchor=tk.SE, relx=1, rely=1, relheight=1, relwidth=1 - vFRAME_relW)
        self._vFrame.place(anchor=tk.NW, relx=0, rely=0, relheight=1, relwidth=vFRAME_relW)

        self._tool = tl.Tool("arty-primary.csv")

        #self._txtVar = tk.StringVar()
        self._txt = tk.Text(self._vFrame)
        self._txt.pack(expand=True, fill=tk.BOTH)

        self._btn = tk.Button(self._mFrame, text="TEST", command=self.temp)
        self._btn.pack()
        self.load_data()

    def temp(self):
        stf = self._tool.get_outliers("Altitude")
        self.replace(stf)
        print("yo")

    def load_data(self):
        try:
            dfstr = self._tool.get_data().to_string()
            self.replace(dfstr)
        except:
            alert.showerror("Error", sys.exc_info())

    def init_vFrame(self):
        pass

    def replace(self, txt):
        self._txt.delete(1.0, "end")
        self._txt.insert(1.0, txt)
