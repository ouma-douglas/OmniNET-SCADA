"""
==========================================================
OmniNET-SCADA
Day 3 - Multi-Threaded Device Simulator
==========================================================

Purpose
-------
Simulates multiple independent field devices transmitting
telemetry simultaneously to the central SCADA server.

Each simulated device operates in its own thread.

Protocols Supported
-------------------
• CSV
• HEX

Devices
-------
M01 -> HEX
M02 -> CSV
M03 -> CSV
M04 -> HEX
"""

import socket
import threading
import random
import time
import binascii

############################################################
# NETWORK CONFIGURATION
############################################################

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 5005

############################################################
# DEVICE CONFIGURATION
############################################################

DEVICES = {

    "M01": {
        "protocol": "HEX",
        "base_temperature": 22.0,
        "interval": 1.5
    },

    "M02": {
        "protocol": "CSV",
        "base_temperature": 24.0,
        "interval": 2.0
    },

    "M03": {
        "protocol": "CSV",
        "base_temperature": 28.0,
        "interval": 1.0
    },

    "M04": {
        "protocol": "HEX",
        "base_temperature": 31.0,
        "interval": 2.5
    }

}

############################################################
# TELEMETRY GENERATION
############################################################

def generate_telemetry(device_id, config):
    """
    Creates realistic telemetry values.
    """

    temperature = config["base_temperature"] + random.uniform(-1.5, 1.5)

    humidity = random.uniform(70.0, 85.0)

    if temperature >= 29.5:
        status = "OVERHEAT"
    else:
        status = "NORMAL"

    return temperature, humidity, status

############################################################
# PACKET ENCODING
############################################################

def build_packet(device_id, config):
    """
    Creates either a CSV packet or HEX packet.
    """

    temperature, humidity, status = generate_telemetry(
        device_id,
        config
    )

    csv_string = (
        f"{device_id},"
        f"{temperature:.1f},"
        f"{humidity:.1f},"
        f"{status}"
    )

    if config["protocol"] == "CSV":

        packet = "CSV:" + csv_string

    else:

        hex_string = binascii.hexlify(
            csv_string.encode("utf-8")
        ).decode("utf-8")

        packet = "HEX:" + hex_string

    return packet

############################################################
# DEVICE THREAD
############################################################

def simulate_device(device_id, config):
    """
    Background worker representing one field device.
    """

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    print(
        f"[{device_id}] Thread Started "
        f"({config['protocol']})"
    )

    while True:

        try:

            packet = build_packet(
                device_id,
                config
            )

            client_socket.sendto(

                packet.encode("utf-8"),

                (TARGET_HOST, TARGET_PORT)

            )

            print()

            print(f"[{device_id}] Packet Sent")

            print(packet)

            print("-" * 60)

            time.sleep(
                config["interval"]
            )

        except Exception as e:

            print(
                f"[{device_id}] Error: {e}"
            )

            break

############################################################
# MAIN PROGRAM
############################################################

def main():

    print("=" * 70)
    print("OmniNET Multi-Device Simulator")
    print("=" * 70)

    print()

    print(f"Target Server : {TARGET_HOST}:{TARGET_PORT}")

    print(f"Devices Online: {len(DEVICES)}")

    print()

    threads = []

    ########################################################
    # START ALL DEVICES
    ########################################################

    for device_id, config in DEVICES.items():

        thread = threading.Thread(

            target=simulate_device,

            args=(device_id, config),

            daemon=True,

            name=device_id

        )

        thread.start()

        threads.append(thread)

    ########################################################
    # KEEP MAIN THREAD ALIVE
    ########################################################

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        print()

        print("Simulation Stopped.")

############################################################

if __name__ == "__main__":

    main()