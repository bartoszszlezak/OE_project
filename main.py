from tkinter import *
from src.gui.menu_gui import MyWindow


if __name__ == '__main__':
    window = Tk()
    mywin = MyWindow(window)
    window.title('Genetic algorithm')
    window.geometry("500x800+10+10")
    window.resizable(False, False)
    window.mainloop()
