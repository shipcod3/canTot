from sploitkit import *
import can

class spam_bus(Module):
    """ This module will spam the bus with messages using an extended ID 0xc0ffee.

    Author:  shipcod3 # canTot module
    Credits: python-can example
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
        print("[+] Spamming the bus")
        for i in range(256):
            msg = can.Message(arbitration_id=0xc0ffee, data=[0x0A, i, 0, 1, 3, 1, 4, 1], is_extended_id=True)
            bus.send(msg)

