import os as os
import sys as sys
from visualiser import App


DATA_PATH = "data"


def main():
    print("Enter command")
    while True:
        command_line = input().split(" ")
        command = command_line[0]

        if command == "clean":
            pass

        elif command == "visual":
            app = App()
            app.mainloop()

        elif command == "data":
            files = os.listdir(DATA_PATH)
            print("Available data:")
            for name in files:
                print(name)

        elif command == "exit":
            sys.exit(0)

        else:
            print("Command not recognised")


if __name__ == '__main__':
    main()
