import pyvisa

class Vitrek:
  
  def __init__(self, testType, vMax):
    self.testType = testType
    self.vMax = vMax
    
   
rm = pyvisa.ResourceManager()
v = rm.open_resource("ASRL10::INSTR")
v.baud_rate = 9600
v.data_bits = 8
v.parity = pyvisa.constants.Parity.none
v.stop_bits = pyvisa.constants.StopBits.one
#v.read_termination = '\r'
v.timeout = 5000

v.write("NOSEQ;ADD,ACEZ,100.0,60.0,1.5,3.0,0.0,0.005,ABORT;RUN")
v.query("RUN?")

v.close()
