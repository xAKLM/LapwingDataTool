import sys as sys
from gui import App


def main():
    try:
        app = App()
        app.mainloop()
    except:
        print(sys.exc_info())
        input()
        sys.exit(-1)
    sys.exit(0)


if __name__ == '__main__':
    main()
