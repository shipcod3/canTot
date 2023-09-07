import can
import time

# Define the CAN bus interface and channel
can_interface = 'socketcan'  # Use 'socketcan' for Linux, adjust for other platforms
channel = 'can0'             # Adjust based on your hardware configuration

# Define the target arbitration ID and data
target_arbitration_id = 0x7DF
target_data = [0x02, 0x11, 0x01]

# Initialize the CAN bus interface
bus = can.interface.Bus(channel=channel, bustype=can_interface)

while True:
    try:
        message = bus.recv()
        if message.arbitration_id == target_arbitration_id and message.data == target_data:
            print("ECU hard reset detected!")

    except KeyboardInterrupt:
        break

# Close the CAN bus interface when done
bus.shutdown()
