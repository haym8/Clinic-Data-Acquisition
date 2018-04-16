'''
Modules Requiried
[x] Selection of Com Port for Each Instrument
[x] Selection of Test Type
[ ] Start Button
[ ] Stop Button
[ ] Text field stating Breakdown Voltage
[ ] Plots
'''

from Tkinter import *
import Tkinter as ttk
from ttk import *
import serial
from enum import Enum
#import keithley2.py
#import keithley6.py
#import vitrek.py

class TestType(Enum):
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
window.geometry("400x400")

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
              value=TestType.astm.value)
sel2 = Radiobutton(window, 
              text="DoD",
              variable=v,
              value=TestType.dod.value)
sel1.grid(column=0, row=7, sticky=W, padx=20)
sel2.grid(column=0, row=8, sticky=W, padx=20)

# Run mainloop
window.mainloop()
