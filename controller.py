'''
Modules Requiried
[x] Selection of Com Port for Each Instrument
[x] Selection of Test Type
[x] Start Button
[x] Stop Button
[ ] Text field stating Breakdown Voltage
[ ] Plots
[ ] Serial Number Generation
'''

from Tkinter import *
import Tkinter as ttk
from ttk import *
import serial
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from enum import Enum
import os
#import keithley2.py
#import keithley6.py
#import vitrek.py

PATH = "C:\"

class Test(Enum):
    astm = 1
    dod = 2

ports = ["COM%s" % (i+1) for i in range(256)]
comPorts = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        comPorts.append(port)
    except serial.SerialException:
        pass

# Set up window
window = Tk()
window.title("Dielectric Breakdown Testing")
window.geometry("600x600")

# Set up for dropdown menus
com = StringVar(window)
com.set("COM1")

# Vitrek Menu
v_com = StringVar(window)
v_com.set("COM1")
v_lbl = Label(window, text="Vitrek Serial Port", font=("Times New Roman", 12))
v_lbl.grid(column=0, row=0)
v_drop = OptionMenu(window, v_com, *comPorts)
v_drop.grid(column=1, row=0)
space = Label(window, text = " ", font=("Times New Roman", 3))
space.grid(column=0, row=1)

# DMM Menu
dmm_com = StringVar(window)
dmm_com.set("COM1")
dmm_lbl = Label(window, text="DMM Serial Port", font=("Times New Roman", 12))
dmm_lbl.grid(column=0, row=2)
dmm_drop = OptionMenu(window, dmm_com, *comPorts)
dmm_drop.grid(column=1, row=2)
space = Label(window, text = " ", font=("Times New Roman", 3))
space.grid(column=0, row=3)


# Ammeter Menu
amm_com = StringVar(window)
amm_com.set("COM1")
amm_lbl = Label(window, text="Ammeter Serial Port", font=("Times New Roman", 12))
amm_lbl.grid(column=0, row=4)
amm_drop = OptionMenu(window, amm_com, *comPorts)
amm_drop.grid(column=1, row=4)
space = Label(window, text = " ", font=("Times New Roman", 3))
space.grid(column=0, row=5)

# Select Test Type
v = IntVar()
lbl = Label(window, text="Choose a test type:", justify = LEFT)
lbl.grid(column=0, row=6, sticky=W)
sel1 = Radiobutton(window, 
              text="ASTM",
              variable=v,
              value=Test.astm.value)
sel2 = Radiobutton(window, 
              text="DoD",
              variable=v,
              value=Test.dod.value)
sel1.grid(column=0, row=7, sticky=W, padx=20)
sel2.grid(column=0, row=8, sticky=W, padx=20)

# Embedded Plot
f = Figure(figsize=(3.5,3.5), dpi=100)
a = f.add_subplot(111)
###### Replace this with relevant data ######
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
canvas = FigureCanvasTkAgg(f, master=window)
##### Edit location of plot ########
canvas.get_tk_widget().grid(column=2, row=9)
canvas.draw()



# Run mainloop
window.mainloop()
