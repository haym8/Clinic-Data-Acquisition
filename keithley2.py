import pyvisa
import matplotlib.pyplot as plt
import numpy as np
import time

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
times = []


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

for j in range(1,10):
    k.write(":SAMP:COUNT " + str(j))
    for i in range(1000/j):
        a = time.time()
        voltages.append(k.query(":READ?"))
        b = time.time() - a
        times.append(b)

    print "Sample Count: " + str(j)
    print "Average Time Off: " + str(np.mean(times))
    print "Total Time: " + str(np.sum(times))
    print "Sampling Rate: " + str(1000/np.sum(times))

    times = []
    
for j in range(len(voltages)):
    v = voltages[j].encode("ascii")
    vn = v.split(",")
    for elem in vn:
        volt_form.append(float(elem))

k.close()

#plt.plot(volt_form)
#plt.show()
