import can

# Create a bus instance
can_bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

# Create a UDS message with a known service ID
msg = can.Message(arbitration_id=0x7DF, data=[0x3E, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77], extended_id=True)

# Send the message on the bus
can_bus.send(msg)

# Receive a response from the vehicle
response = can_bus.recv()

# Print the response message
print(response)
