from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
import time

class rx8_rpm_fuzzer(Module):
    """ This module sends out CAN data to a Mazda RX8 instrument cluster.

    Author:  shipcod3
    Credits: skpang
    Reference: https://github.com/skpang/PiCAN-Python-examples/blob/master/cluster_rpm.py
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
                for rpm in range (0,130):
                    frame = can.Frame(0x201)
                    frame.data = [rpm,0,0,0,0,0,0,0]
                    dev.send(frame)
                    time.sleep(0.5)
        except KeyboardInterrupt:
            print('\n\rKeyboard interrtupt')
        pass
