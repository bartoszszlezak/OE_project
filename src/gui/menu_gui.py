from tkinter import *
from PIL import ImageTk, Image
import time
from src.plot import plot
from src.configuration import *
from src.generic_algorithm.algorithm.algorithm import run_algorithm

class MyWindow:
    def __init__(self, win):


        #Background
        self.image = Image.open("src/gui/oe5.jpg")
        self.img = self.image.resize((500, 800))
        self.bg = ImageTk.PhotoImage(self.img)
        self.label_bg = Label(win, image=self.bg)
        self.label_bg.place(x=0, y=0)

        #Colours
        label_fg_color = "black"
        label_bg_color = "white"

        input_fg_color = "black"
        input_bg_color = "white"

        dropBox_fg_color = "black"
        dropBox_bg_color = "white"




        #Labels

        self.lbl1 = Label(win, text='Start: ')
        self.lbl2 = Label(win, text='End: ')
        self.lbl3 = Label(win, text='Precision: ')
        self.lbl4 = Label(win, text='Pop size: ')
        self.lbl5 = Label(win, text='Epochs number: ')
        self.lbl6 = Label(win, text='Selection type: ')
        self.lbl7 = Label(win, text='Selection percent: ')
        self.lbl8 = Label(win, text='Selection no groups: ')
        self.lbl9 = Label(win, text='Crossover type: ')
        self.lbl10 = Label(win, text='Crossover probability: ')
        self.lbl11 = Label(win, text='Mutation type: ')
        self.lbl12 = Label(win, text='Mutation probabliliy: ')
        self.lbl13 = Label(win, text='Inversion probability: ')
        self.lbl14 = Label(win, text='Elite percent: ')
        self.lbl15 = Label(win, text='Algorithm goal: ')

        self.lbl1.place(x=100, y=40)
        self.lbl2.place(x=100, y=80)
        self.lbl3.place(x=100, y=120)
        self.lbl4.place(x=100, y=160)
        self.lbl5.place(x=100, y=200)
        self.lbl6.place(x=100, y=240)
        self.lbl7.place(x=100, y=280)
        self.lbl8.place(x=100, y=320)
        self.lbl9.place(x=100, y=360)
        self.lbl10.place(x=100, y=400)
        self.lbl11.place(x=100, y=440)
        self.lbl12.place(x=100, y=480)
        self.lbl13.place(x=100, y=520)
        self.lbl14.place(x=100, y=560)
        self.lbl15.place(x=100, y=600)


        self.lbl1.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl2.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl3.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl4.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl5.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl6.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl7.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl8.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl9.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl10.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl11.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl12.configure(foreground=label_fg_color, background=label_bg_color)
        self.lbl13.configure(foreground=label_fg_color, background=label_bg_color)



        #Inputs
        self.start=Entry(bd=3)
        self.end=Entry()
        self.prec=Entry()
        self.pop_size = Entry()
        self.epchs_num = Entry()
        self.sel_perc = Entry()
        self.sel_no_groups = Entry()
        self.cross_prob = Entry()
        self.mut_prob = Entry()
        self.inv_prob = Entry()
        self.elite_percent = Entry()



        self.start.configure(foreground=input_fg_color, background=input_bg_color)
        self.end.configure(foreground=input_fg_color, background=input_bg_color)
        self.prec.configure(foreground=input_fg_color, background=input_bg_color)
        self.pop_size.configure(foreground=input_fg_color, background=input_bg_color)
        self.epchs_num.configure(foreground=input_fg_color, background=input_bg_color)
        self.sel_perc.configure(foreground=input_fg_color, background=input_bg_color)
        self.sel_no_groups.configure(foreground=input_fg_color, background=input_bg_color)
        self.cross_prob.configure(foreground=input_fg_color, background=input_bg_color)
        self.mut_prob.configure(foreground=input_fg_color, background=input_bg_color)
        self.inv_prob.configure(foreground=input_fg_color, background=input_bg_color)
        self.elite_percent.configure(foreground=input_fg_color, background=input_bg_color)

        self.start.place(x=250, y=40, w=50)
        self.end.place(x=250, y=80, w=50)
        self.prec.place(x=250, y=120, w=50)
        self.pop_size.place(x=250, y=160, w=50)
        self.epchs_num.place(x=250, y=200, w=50)
        self.sel_perc.place(x=250, y=280, w=50)
        self.sel_no_groups.place(x=250, y=320, w=50)
        self.cross_prob.place(x=250, y=400, w=50)
        self.mut_prob.place(x=250, y=480, w=50)
        self.inv_prob.place(x=250, y=520, w=50)
        self.elite_percent.place(x=250, y=560, w=50)

        #Dropbox

        #Options
        self.optionsSelection = [
            "SELECTION_BEST",
            "SELECTION_TOURNAMENT",
            "SELECTION_ROULETTE"
        ]
        self.optionsCrossover = [
            "CROSSOVER_HOMOGENOUS",
            "CROSSOVER_SINGLE_POINT",
            "CROSSOVER_DOUBLE_POINT"

        ]
        self.optionsMutation = [
            "MUTATION_BOUNDARY",
            "MUTATION_SINGLE_POINT",
            "MUTATION_DOUBLE_POINT"
        ]

        self.optionsMinMax = [
            "MAXIMUM",
            "MINIMUM",
        ]

        #SelectedOptions
        self.selectedSelection = StringVar()
        self.selectedCrossover = StringVar()
        self.selectedMutation = StringVar()
        self.selectedGoal = StringVar()



        self.dropBox1 = OptionMenu(win, self.selectedSelection, *self.optionsSelection)
        self.dropBox1.place(x=250, y=240, w=200)
        self.dropBox1.configure(foreground=dropBox_fg_color, background=dropBox_bg_color )

        self.dropBox2 = OptionMenu(win, self.selectedCrossover, *self.optionsCrossover)
        self.dropBox2.place(x=250, y=360, w=200)
        self.dropBox2.configure(foreground=dropBox_fg_color, background=dropBox_bg_color )


        self.dropBox3 = OptionMenu(win, self.selectedMutation, *self.optionsMutation)
        self.dropBox3.place(x=250, y=440, w=200)
        self.dropBox3.configure(foreground=dropBox_fg_color, background=dropBox_bg_color )


        self.dropBox4 = OptionMenu(win, self.selectedGoal, *self.optionsMinMax)
        self.dropBox4.place(x=250, y=600, w=200)
        self.dropBox4.configure(foreground=dropBox_fg_color, background=dropBox_bg_color )



        self.b1=Button(win, text='Calculate', command = lambda:self.calculate(win))
        self.b1.place(x=200, y=725,w=100,h=50)

    def configure(self):

        conf = Config()

        conf.start = int(self.start.get()) if self.start.get() else  START
        conf.end = int(self.end.get()) if self.end.get() else END
        conf.precision = int(self.prec.get()) if self.prec.get() else PRECISION
        conf.pop_size = int(self.pop_size.get()) if self.pop_size.get() else POPULATION_SIZE
        conf.no_epochs = int(self.epchs_num.get()) if self.epchs_num.get() else NUMBER_OF_EPOCHS
        conf.selection_type = self.selectedSelection.get() or SELECTION_ROULETTE
        conf.selection_percent = float(self.sel_perc.get()) if self.sel_perc.get() else SELECTION_PERCENT
        conf.selection_no_groups = int(self.sel_no_groups.get()) if self.sel_no_groups.get() else SELECTION_NO_GROUPS
        conf.crossover_type = self.selectedCrossover.get() or CROSSOVER_SINGLE_POINT
        conf.crossover_probability = float(self.cross_prob.get()) if self.cross_prob.get() else CROSSOVER_PROB
        conf.mutation_type = self.selectedMutation.get() or MUTATION_SINGLE_POINT
        conf.mutation_probability = float(self.mut_prob.get()) if self.mut_prob.get() else MUTATION_PROB
        conf.inversion_probability = float(self.inv_prob.get()) if self.inv_prob.get() else INVERSION_PROB
        conf.elite_percent = float(self.elite_percent.get()) if self.elite_percent.get() else ELITE_PERCENT
        conf.algorithm_goal = self.selectedGoal.get() or MINIMUM

        return conf



    def calculate(self,win):


        conf = self.configure()

        start = time.time()
        result_fitness, result_average, result_standard_deviation = run_algorithm(conf)
        end = time.time()

        pure_fitness = [res[2] for res in result_fitness]

        plt.title("Wartość funkcji w kolejnej iteracji")
        plot(pure_fitness)
        plt.title("Srednia wartość funkcji w kolejnej iteracji")
        plot(result_average)
        plt.title("Odchylenie standardowe w kolejnej iteracji")
        plot(result_standard_deviation)


        results = {
            "x1": round(result_fitness[len(result_fitness) - 1][0],2) ,
            "x2": round(result_fitness[len(result_fitness) - 1][1],2),
            "y": round(result_fitness[len(result_fitness) - 1][2],2),
        }



        timer = end - start


        self.openNewWindow(win,timer,results)


    def openNewWindow(self,win,timer,results):
        newWindow = Toplevel(win)
        newWindow.title("Wyniki")
        newWindow.geometry("200x75")
        t = "Solution was found in: " + str(round(timer,3)) + " s"
        Label(newWindow,
              text=t).pack()
        Label(newWindow,
              text=f"Ekstremum: f({results['x1']},{results['x2']}) = {results['y']}").pack()


