from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class candump(Module):
    """ This module dumps everything on the bus.

    Author:  shipcod3
    Credits: Eric Evenchick (pyvit module and example) 
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
        while True:
            print(dev.recv())
        pass
