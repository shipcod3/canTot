from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan
from time import sleep
from math import ceil
from random import shuffle
import codecs

class uds_sec_access(Module):
    """ This module will scan a vehicle for UDS services using Security Access.
    
    Author:  shipcod3
    Credits: ps1337
    Reference: https://github.com/ps1337/automotive-security-research/blob/master/helpers/udsSecAccess.py
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

        def init():
            global dev
            dev = socketcan.SocketCanDev(self.config.option('INTERFACE').value)
            dev.start()
            return dev


        def tryBuildPacket(dataTuple):
            packet = None
            try:
                # convert id to hexvalue
                # convert data to list of bytes
                packet = can.Frame(
                    arb_id=int(dataTuple[0], 16),
                    data=list(bytearray.fromhex(dataTuple[1])))
            except ValueError as e:
                if "Arbitration ID out of range" in str(e):
                    return False, None
                else:
                    raise
            return True, packet


        dev = init()

        for x in range(255):
            for i in range(255):
                hexData = "0327" + hex(i).replace("0x", "") + "0" + hex(x).replace(
                    "0x", "")
                while len(hexData) < 16:
                    hexData += "0"
                arbit_to_fuzz = hex(self.config.option('ARBID').value)
                retVal = tryBuildPacket((arbit_to_fuzz, hexData))
                packet_ok = retVal[0]
                packet = retVal[1]

                if packet_ok:
                    print(packet)
                    dev.send(packet)
                    sleep(0.1)
                else:
                    print("[-] Damaged packet!")
