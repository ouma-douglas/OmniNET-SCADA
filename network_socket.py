"""
==========================================================
OmniNET-SCADA
Day 3 - Central SCADA UDP Server
==========================================================

Purpose
-------
This module represents the central SCADA server.

Responsibilities:
    • Listen continuously on UDP Port 5005
    • Receive telemetry packets
    • Pass packets to the Unified Ingestion Engine
    • Display standardized telemetry

The server does NOT care whether incoming packets are
CSV or HEX. That responsibility belongs to
ingestion_engine.py.
"""

import socket
import json

from ingestion_engine import parse_telemetry


###########################################################
# NETWORK CONFIGURATION
###########################################################

HOST = "127.0.0.1"

PORT = 5005

BUFFER_SIZE = 1024


###########################################################
# SERVER INITIALIZATION
###########################################################

def start_scada_server():

    """
    Starts the central OmniNET SCADA server.
    """

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    try:

        server_socket.bind((HOST, PORT))

        print("=" * 70)
        print("        OmniNET-SCADA Central Server")
        print("=" * 70)

        print(f"Listening on {HOST}:{PORT}")

        print("Protocol Support:")
        print("   ✓ CSV")
        print("   ✓ HEX")

        print("\nWaiting for telemetry...\n")

    except Exception as e:

        print(f"Failed to bind socket:\n{e}")

        return

    #######################################################
    # MAIN SERVER LOOP
    #######################################################

    while True:

        try:

            ################################################
            # Receive packet
            ################################################

            data, address = server_socket.recvfrom(BUFFER_SIZE)

            raw_packet = data.decode("utf-8")

            print("=" * 70)

            print(f"Packet received from {address}")

            print()

            print("RAW DATA")

            print(raw_packet)

            print()

            ################################################
            # Pass packet into abstraction layer
            ################################################

            normalized_data = parse_telemetry(raw_packet)

            ################################################
            # Display standardized JSON
            ################################################

            print("STANDARDIZED TELEMETRY")

            print(

                json.dumps(

                    normalized_data,

                    indent=4

                )

            )

            print()

        except KeyboardInterrupt:

            print("\nStopping OmniNET SCADA Server...")

            break

        except Exception as e:

            print(f"\nReception Error: {e}")

            continue

    server_socket.close()


###########################################################
# ENTRY POINT
###########################################################

if __name__ == "__main__":

    start_scada_server()