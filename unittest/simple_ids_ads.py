# simple script for anomaly detection for CAN Bus
# Monitors incoming messages and checks their CAN IDs against a predefined list of allowed IDs. 
# If a message with an unexpected ID is received, it prints an anomaly detection message.

import can

# Define a list of allowed CAN message IDs
allowed_ids = [0x100, 0x200, 0x300]

# Create a CAN bus interface object
can_bus = can.interface.Bus(bustype='socketcan', channel='can0')

def process_can_message(msg):
    """
    Process and analyze incoming CAN messages.
    """
    if msg.arbitration_id not in allowed_ids:
        print(f"Anomaly Detected: Unexpected CAN ID - {hex(msg.arbitration_id)}")

# Main loop to monitor the CAN bus
try:
    while True:
        message = can_bus.recv()
        process_can_message(message)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting.")
finally:
    can_bus.shutdown()