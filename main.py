import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
