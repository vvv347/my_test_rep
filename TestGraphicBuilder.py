from tkinter import filedialog
from tkinter import *
import math
import csv

root = Tk()
root.title("ParabollaBuilder")
root.geometry("600x600")

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.directory = None
        
    def create_widgets(self):
        self.lbl = Label(self, text = "Программа создает тестовую функцию")
        self.lbl.grid(row = 0, column = 0, columnspan = 1, sticky = N)

        self.entryX = Entry(self, textvariable = IntVar(self, value = "1"))
        self.entryX.grid(row = 1, column = 1, columnspan = 1, sticky = W)

        self.entryZ = Entry(self, textvariable = IntVar(self, value = "1"))
        self.entryZ.grid(row = 2, column = 1, columnspan = 1, sticky = W)

        self.lblX = Label(self, text = "Xmax")
        self.lblX.grid(row = 1, column = 0, columnspan = 1, sticky = W)

        self.lblX = Label(self, text = "Zmax")
        self.lblX.grid(row = 2, column = 0, columnspan = 1, sticky = W)

        self.bttnchoose = Button(self, text = "Выбрать папку для файла")
        self.bttnchoose["command"] = self.choose_path
        self.bttnchoose.grid(row = 4, column = 0, sticky = W)

        self.bttnsave = Button(self, text = "Создать файл")
        self.bttnsave["command"] = self.create_file
        self.bttnsave.grid(row = 4, column = 1, sticky = W)

        self.lblstep = Label(self, text = "Шаг")
        self.lblstep.grid(row = 3, column = 0, sticky = W)

        self.entrystep = Entry(self, textvariable = IntVar(self, value = "0.1"))
        self.entrystep.grid(row = 3, column = 1, sticky = W)
        
    def choose_path(self):
        self.directory = filedialog.askdirectory()

    def create_file(self):
        out = [["X","Y","Z"]]
        
        b = float(self.entryX.get()) / 2.0
        c = float(self.entryZ.get())
        a = abs(c) * 4.0 / (b * b * 4)
        step = float(self.entrystep.get())
        x = 0.0
        print(self.directory)
        while x <= (2 * b):
            out.append([x, 0, a * (x - b) * (x - b) - c])
            x += step

        with open(self.directory + "/TestFunc.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(out)
        
app = Application(root)
root.mainloop()

#folder_selected = filedialog.askdirectory()

