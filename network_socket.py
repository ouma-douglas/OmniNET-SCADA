import socket
import json
from ingestion_engine import parse_hex_payload, parse_csv_payload  # Reusing Day 1 logic

# Network configurations
HOST = '127.0.0.1'  # Localhost loops back inside your computer safely
PORT = 5005         # Unprivileged port reserved for custom data streams

def start_scada_server():
    # Initialize a UDP (User Datagram Protocol) socket for fast streaming
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        server_socket.bind((HOST, PORT))
        print(f"📡 OmniNET SCADA Network Server Active and Online!")
        print(f"Listening continuously for incoming telemetry streams on {HOST}:{PORT}...\n")
        print("-" * 75)
    except Exception as e:
        print(f"❌ Failed to bind to server port: {e}")
        return

    while True:
        try:
            # Receive incoming byte packets up to 1024 bytes buffer size
            data, addr = server_socket.recvfrom(1024)
            raw_payload = data.decode('utf-8')
            print(f"📥 Received raw packet from {addr}: {raw_payload}")
            
            # Central Parsing Abstraction Layer
            parsed_data = {}
            if raw_payload.startswith("CSV:"):
                # Strip the "CSV:" prefix and parse
                parsed_data = parse_csv_payload(raw_payload[4:])
            elif raw_payload.startswith("HEX:"):
                # Strip the "HEX:" prefix and parse
                parsed_data = parse_hex_payload(raw_payload[4:])
            else:
                print("⚠️ Unknown data format received.")
                continue
                
            # Output matching structured JSON telemetry directly to the screen
            print(f"📋 Standardized Telemetry: {json.dumps(parsed_data, indent=2)}")
            print("-" * 75)
            
        except Exception as e:
            print(f"❌ Error processing packet: {e}")

if __name__ == "__main__":
    start_scada_server()