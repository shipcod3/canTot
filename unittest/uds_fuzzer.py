import random
import time

from can import Message
from can.interfaces.interface import Bus

# Create a bus instance
can_bus = Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

# Define the UDS arbitration ID to use for requests
UDS_ARBITRATION_ID = 0x7DF

# Create a function for sending a UDS request with random data
def send_uds_request():
    data = [random.randint(0, 255) for _ in range(8)]
    msg = Message(arbitration_id=UDS_ARBITRATION_ID, data=data)
    can_bus.send(msg)

# Send a random UDS request every second
while True:
    send_uds_request()
    time.sleep(1)
