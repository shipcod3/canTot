from sploitkit import *
import can
import time

class pdo_input_output_controller(Module):
    """ This module will control PDO's input and output over CAN and based of mintynet's PDO Car in a box Disco mode.

    Author:  shipcod3 # canTot module
    Credits: mintynet
    Reference: https://github.com/mintynet/BSidesScotland2019/blob/master/disco-mode/disco-mode.ino
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
            print("[*] Turning the fog lights off")
            fog_off = can.Message(arbitration_id=0x094, data=[0x02,0x0,0x0,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(fog_off)
            time.sleep(1)

            print("[*] Turning the left hand indicator")
            lefthand_indicator = can.Message(arbitration_id=0x094, data=[0x0,0x0,0x40,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(lefthand_indicator)
            time.sleep(1)         

            print("[*] Turning the fog lights on")
            fog_on = can.Message(arbitration_id=0x094, data=[0x04,0x0,0x0,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(fog_on)
            time.sleep(1)

            print("[*] Turning the right hand indicator")
            righthand_indicator = can.Message(arbitration_id=0x094, data=[0x0,0x0,0x80,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(righthand_indicator)
            time.sleep(1)

            print("[*] Turning on the hazard lights")
            hazard_lights = can.Message(arbitration_id=0x094, data=[0x0,0x0,0xC0,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            bus.send(hazard_lights)
        except:
            print("Messages not sent. Module failed!")
