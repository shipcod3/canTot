from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class diagnostic_state(Module):
    """ This module will keep the vehicle in a diagnostic state on loop by sending tester present packet.   

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
        print("[*] Putting the vehicle in a diagnostic state...")
        frame = can.Frame(self.config.option('ARBID').value)
        frame.data = [0x01,0x3E]
        print("Press Ctrl+C to stop or cancel")

        while True:
            dev.send(frame)
        pass
