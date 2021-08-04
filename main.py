import sys as sys
from gui import App
from tool import Tool

def main():
    tool = Tool("arty-primary.csv")
    # try:
    #     app = App()
    #     app.mainloop()
    # except:
    #     print(sys.exc_info())
    #     input()
    #     sys.exit(-1)
    # sys.exit(0)
    print(tool.get_data())
    print("---------------------------------")
    print(tool.get_outliers("Attribute"))
if __name__ == '__main__':
    main()
