from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
import time

class uds_fuzzer(Module):
    """ This module sends diagnostic session control to discover UDS ids.

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
        for i in range (0x00,0x800):
            print("[*] Sending diagnostic session control to >> " + hex(i))
            frame = can.Frame(i)
            frame.data = [0x02,0x10,0x01,0,0,0,0,0]
            dev.send(frame)
            time.sleep(0.5)
            # This module is not yet finished and needs more improvements
        pass
