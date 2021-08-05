import sys
import time
import tkinter as tk
import tkinter.messagebox as alert
import tool as tl


TITLE = "Lapwing Data Tool"
RESOLUTION = "1280x720"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(RESOLUTION)

        # Initialise components
        self._mFrame = tk.Frame(self)
        self._vFrame = tk.Frame(self)
        self._entry = tk.Entry(self._vFrame)
        self._entry.bind("<Return>", lambda event: self.enter(self._entry.get()))
        self._text = tk.Text(self._vFrame)

        self.set_components()

        self._tool = tl.Tool("arty-primary.csv")
        self._btn = tk.Button(self._mFrame, text="TEST", command=self.temp)
        self._btn.pack()

        self.load_data()

    def set_components(self):
        self._mFrame.place(anchor=tk.SE, relx=1, rely=1, relheight=1, relwidth=0.2)
        self._vFrame.place(anchor=tk.NW, relx=0, rely=0, relheight=1, relwidth=0.8)
        self._entry.place(anchor=tk.SE, relx=1, rely=1, height=24, relwidth=1)
        self._text.place(anchor=tk.NW, relx=0, rely=0, height=696, relwidth=1)

    def enter(self, command):
        self.clear_entry()

        if len(command) == 0 or command[0] != '/':
            return

        line = command[1:]
        if line != "test":
            self.handle_error("test is the only implemented command")
        else:
            self.replace_text(line)
            self.after(2000, self.temp)

    def temp(self):
        try:
            stf = self._tool.get_outliers("Altitude")
            self.replace_text(stf)
            print("yo")
        except:
            self.handle_error()

    def load_data(self):
        try:
            dfstr = self._tool.get_data().to_string()
            self.replace_text(dfstr)
        except:
            self.handle_error()

    def init_vFrame(self):
        pass

    def replace_text(self, text):
        self._text.delete(1.0, "end")
        self._text.insert(1.0, text)

    def clear_entry(self):
        self._entry.delete(0, "end")

    @staticmethod
    def handle_error(msg=None):
        alert.showerror("Error", msg if msg is not None else sys.exc_info())
