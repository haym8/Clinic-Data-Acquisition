import pyvisa
import matplotlib.pyplot as plt
import numpy as np
import csv

class Keithley2:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        k = rm.open_resource("ASRL7::INSTR")
        k.baud_rate = 19200
        k.data_bits = 8
        k.parity = pyvisa.constants.Parity.none
        k.stop_bits = pyvisa.constants.StopBits.one
        k.read_termination = '\r'
        k.timeout = 50000
        voltages = []
        volt_form = []
        
    def ready(self):
        k.write("*RST")
        k.write(":FUNC 'VOLT:DC'")
        k.write(":SENS:VOLT:DC:AVER:STAT OFF")
        k.write(":SENS:VOLT:DC:NPLC 0.01")
        k.write(":SENS:VOLT:DC:DIG 4")
        k.write(":RES:RANGE 1")
        k.write(":RES:AVER:STAT OFF")
        k.write(":FORM:ELEM READ")
        k.write(":TRIG:COUN 1")
        k.write(":TRIG:DEL 0.0")
        k.write(":TRIG:SOUR IMM")
        k.write(":SYSTEM:AZERO:STAT OFF")
        k.write(":DISP:ENAB OFF")
        k.write(":SAMP:COUNT 1")
        
    def read(self):
        voltages.append(k.query(":READ?"))

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
                
    def close(self):
        k.close()
