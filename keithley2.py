import pyvisa
import matplotlib.pyplot as plt
import numpy as np
import csv

class Keithley2:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.k = rm.open_resource("ASRL7::INSTR")
        self.k.baud_rate = 19200
        self.k.data_bits = 8
        self.k.parity = pyvisa.constants.Parity.none
        self.k.stop_bits = pyvisa.constants.StopBits.one
        self.k.read_termination = '\r'
        self.k.timeout = 50000
        voltages = []
        volt_form = []
        
    def ready(self):
        self.k.write("*RST")
        self.k.write(":FUNC 'VOLT:DC'")
        self.k.write(":SENS:VOLT:DC:AVER:STAT OFF")
        self.k.write(":SENS:VOLT:DC:NPLC 0.01")
        self.k.write(":SENS:VOLT:DC:DIG 4")
        self.k.write(":RES:RANGE 1")
        self.k.write(":RES:AVER:STAT OFF")
        self.k.write(":FORM:ELEM READ")
        self.k.write(":TRIG:COUN 1")
        self.k.write(":TRIG:DEL 0.0")
        self.k.write(":TRIG:SOUR IMM")
        self.k.write(":SYSTEM:AZERO:STAT OFF")
        self.k.write(":DISP:ENAB OFF")
        self.k.write(":SAMP:COUNT 1")
        
    def read(self):
        voltages.append(self.k.query(":READ?"))

    def convert(self):
        for j in range(len(voltages)):
            v = voltages[j].encode("ascii")
            vn = v.split(",")
            for elem in vn:
                volt_form.append(float(elem))

    def writeToCSV(self, fileLoc):
        with open(fileLoc, "wb") as csvfile:
            writeOut = csv.writer(csvfile, delimiter=',')
            writeOut.writerow(volt_form)
                
    def cl(self):
        self.k.close()
