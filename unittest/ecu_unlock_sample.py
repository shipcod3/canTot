# this module was made by ChatGPT after teaching it how to dev canTot
import can
from pyvit import can
from pyvit.hw import socketcan

class unlock_ecu(Module):
    """ This module unlocks the specified ECU by sending a CAN frame with the
    specified arbitration ID and data on the CAN bus.

    Author: [Your Name]
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
            "Arbitration ID",
            True,
        ): int(0x123),
        Option(
            'DATA',
            "Data",
            False,
        ): List(int, [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08]),
    })

    def run(self):
        dev = socketcan.SocketCanDev(self.config.option('INTERFACE').value)

        dev.start()
        print("[*] Unlocking ECU...")
        frame = can.Frame(self.config.option('ARBID').value, data=self.config.option('DATA').value)
        dev.send(frame)
        pass
