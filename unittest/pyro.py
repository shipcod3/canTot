import can

# UDS Constants for the queries
UDS_READ_DATA_BY_ID = 0x22

# Define mappings for loop table and address formats
LOOP_TABLE = {
    0x00: 'ISOSAEReserved',
    0x01: 'airbag driver side frontal 1st stage',
    0x02: 'airbag left side frontal 1st stage',
    # Add the rest of the loop table mappings here...
}

ACL_TYPES = {
    0x01: 'CAN only',
    0x02: 'ACL Comm Mode 12V',
    # Add more ACL types if needed...
}

PCU_ADDRESS_FORMAT = {
    0x01: '11 bit normal addressing',
    0x02: '11 bit extended addressing',
    # Add more address formats here...
}

def send_uds_message(bus, can_id, data):
    """Send a UDS message over CAN bus and receive the response."""
    message = can.Message(arbitration_id=can_id, data=data, is_extended_id=False)
    bus.send(message)
    
    response = bus.recv(timeout=1)  # Wait for a response, with 1-second timeout
    if response:
        return response.data
    else:
        raise TimeoutError("No response from the CAN bus.")

def read_data_by_id(bus, src_id, dst_id, data_id):
    """Read data by ID (UDS Service 0x22) from a control unit."""
    data = [UDS_READ_DATA_BY_ID] + data_id  # 0x22 followed by data ID
    return send_uds_message(bus, src_id, data)

def print_vin(vin):
    """Print VIN information from the vehicle."""
    vin_str = ''.join([chr(byte) for byte in vin])
    print(f"VIN: {vin_str}")

def print_loop_table(loop_id):
    """Print loop table information about pyrotechnic devices."""
    print(f"Loop info ({loop_id[2]} pyrotechnic devices):")
    for i in range(3, len(loop_id), 2):
        device_code = loop_id[i]
        if device_code in LOOP_TABLE:
            status = 'Good' if loop_id[i + 1] == 0 else f"Fail ({loop_id[i + 1]})"
            print(f"  {device_code} | {LOOP_TABLE.get(device_code, '<<UNKNOWN>>')} | Status: {status}")

def main():
    can_interface = 'can0'  # Adjust to your CAN interface
    src_id = 0x7f1  # Example CAN ID
    dst_id = 0x7f9  # Example destination CAN ID

    try:
        bus = can.interface.Bus(can_interface, bustype='socketcan')
        print("Gathering Data...")

        # Query VIN
        vin = read_data_by_id(bus, src_id, dst_id, [0xF1, 0x90])
        print_vin(vin)

        # Query pyrotechnic control unit information
        no_of_pcus = read_data_by_id(bus, src_id, dst_id, [0xFA, 0x00])
        no_of_iso_version = read_data_by_id(bus, src_id, dst_id, [0xFA, 0x01])
        address_format = read_data_by_id(bus, src_id, dst_id, [0xFA, 0x02])
        loopid = read_data_by_id(bus, src_id, dst_id, [0xFA, 0x06])

        print_loop_table(loopid)

        print(f"Number of PCUs in vehicle: {no_of_pcus[0]}")
        print(f"Address format: {PCU_ADDRESS_FORMAT.get(address_format[0], 'Unknown')}")
        print(f"ISO26021 standard version: {no_of_iso_version[0]}")
        print(f"Number of pyrotechnic charges: {loopid[2]}")
        print(f"ACL type: {ACL_TYPES.get(loopid[0], 'Unknown')}")
        print(f"ACL type version: {loopid[1]}")

    except can.CanError as e:
        print(f"CAN bus error: {e}")
    except TimeoutError as e:
        print(f"Timeout: {e}")

if __name__ == '__main__':
    main()
