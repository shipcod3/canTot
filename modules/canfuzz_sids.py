from sploitkit import *
import can

class canfuzz_sids(Module):
    """ This module will fuzz SIDs on the CAN Bus.

    Author:  shipcod3 # canTot module
    Credits: carfucar and will-caruana [https://github.com/will-caruana/CHVpi]
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
        bus = can.interface.Bus(bustype="socketcan", channel=self.config.option('INTERFACE').value)
        print("[+] Fuzzing the SIDs")
        arb_id = self.config.option('ARBID').value
        for sids in range(0,0x100):
            msg = can.Message(arbitration_id=arb_id, data=[0x02, sids, 0, 0, 0, 0, 0, 0], is_extended_id=False)
            bus.send(msg)

