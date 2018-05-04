import pyvisa

class Vitrek:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.v = self.rm.open_resource("ASRL10::INSTR")
        self.v.baud_rate = 9600
        self.v.data_bits = 8
        self.v.parity = pyvisa.constants.Parity.none
        self.v.stop_bits = pyvisa.constants.StopBits.one
        #self.v.read_termination = '\r\n'
        self.v.write_termination = '\r\n'
        self.v.set_visa_attribute(pyvisa.constants.VI_ATTR_ASRL_FLOW_CNTRL,
                                  pyvisa.constants.VI_ASRL_FLOW_RTS_CTS)
        self.v.timeout = 5000

    def sendTest(self, testType, voltType, voltMax):
        stringSend = ""
        if voltType == "DC":
            stringSend = "NOSEQ;ADD,DCEZ,"+str(voltMax)+","+str(voltMax/500.0)+",5.0,0.0,0.005,ABORT;RUN"
        elif voltType == "AC":
            stringSend = "NOSEQ;ADD,ACEZ,"+str(voltMax)+",60.0,"+str(voltMax/500.0)+",3.0,0.0,0.005,ABORT;RUN"
            
        self.v.write(stringSend)

    def getRunning(self):
        if self.v.query("RUN?"):
            return True
        else:
            return False
        
    def getResults(self):
        res = self.v.query("STEPRSLT?,1")
        return res
        
    def cl(self):
        self.v.close()
