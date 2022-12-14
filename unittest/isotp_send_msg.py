import can
from can.interfaces.interface import Bus
from can.protocols import isotp

# Create a CAN bus instance
can_bus = Bus(channel='vcan0', bustype='socketcan')

# Create an ISO-TP stack on top of the CAN bus
isotp_stack = isotp.Stack(bus=can_bus,
                          tx_id=0x123,
                          rx_id=0x456,
                          rx_flow_control_timeout=0.1,
                          rx_consecutive_frame_timeout=0.1)

# Create a message to send on the ISO-TP stack
msg = isotp.Message(data=[0, 1, 2, 3, 4, 5, 6, 7])

# Send the message on the ISO-TP stack
isotp_stack.send(msg)
