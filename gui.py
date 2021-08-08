import sys
import time
import tkinter as tk
import tkinter.messagebox as alert
import tool as tl


TITLE = "Lapwing Data Tool"
RESOLUTION = "1280x720"
DEFAULT_FILENAME = "arty-primary.csv"


class App(tk.Tk):
    _tool = None

    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(RESOLUTION)

        # Running setup
        self._data_str = tk.StringVar()
        self._data_str.set(DEFAULT_FILENAME)
        self.open_tool()

        # Initialise components
        self._mFrame = tk.Frame(self)
        self._vFrame = tk.Frame(self)
        self._entry = tk.Entry(self._vFrame)
        self._text = tk.Text(self._vFrame)
        self._data_label = tk.Label(self._mFrame, textvariable=self._data_str)
        self.configure_components()

        # Final setup
        self.replace_text(f"Welcome to the {TITLE} app!")
        self.bind("/", lambda event: self.focus_entry())

    def configure_components(self):
        # Menu frame
        self._mFrame.place(anchor=tk.SE, relx=1, rely=1, relheight=1, relwidth=0.2)
        self._data_label.pack(anchor=tk.N, ipady=20)
        # Visual frame
        self._vFrame.place(anchor=tk.NW, relx=0, rely=0, relheight=1, relwidth=0.8)
        self._entry.place(anchor=tk.SE, relx=1, rely=1, height=24, relwidth=1)
        self._entry.bind("<Return>", lambda event: self.entry_command(self._entry.get()))
        self._text.place(anchor=tk.NW, relx=0, rely=0, height=696, relwidth=1)

    def open_tool(self):
        self._tool = tl.Tool(self._data_str.get())

    def entry_command(self, command):
        self.clear_entry()
        if len(command) == 0 or command[0] != '/':
            return
        line = command[1:]
        if line == "asd":
            self.replace_text(self._tool.get_outliers("altitude"))
        self.replace_text(line)

    def replace_text(self, text):
        try:
            self._text.configure(state="normal")
            self._text.delete(1.0, "end")
            self._text.insert(1.0, text)
            self._text.configure(state="disabled")
        except:
            self.handle_error()

    def clear_entry(self):
        self._entry.delete(0, "end")

    def focus_entry(self):
        self._entry.focus_force()
        if not self._entry.get():
            self._entry.insert(0, '/')

    @staticmethod
    def handle_error(msg=None):
        alert.showerror("Error", msg if msg is not None else sys.exc_info())
