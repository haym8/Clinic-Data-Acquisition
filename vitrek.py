import pyvisa

class Vitrek:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        v = rm.open_resource("ASRL10::INSTR")
        v.baud_rate = 9600
        v.data_bits = 8
        v.parity = pyvisa.constants.Parity.none
        v.stop_bits = pyvisa.constants.StopBits.one
        v.read_termination = '\r\n'
        v.timeout = 5000

    def sendTest(self, testType, voltType, voltMax):
        if voltType = "DC":
            voltType = "DCEZ"
        elif voltType = "AC":
            voltType = "ACEZ"
            
        v.write("NOSEQ;ADD," +
                voltType +
                "," + str(voltMax)  +
                ",60.0," + (voltMax/500.0) +
                ",3.0,0.0,0.005,ABORT;RUN")

    def getPass(self):
        res = v.query("STEPRSLT?,1")
        
    def close(self):
        v.close()
