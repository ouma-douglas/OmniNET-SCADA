import socket
import time
import random

HOST = '127.0.0.1'
PORT = 5005

def run_simulator():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("🚀 Simulated Substation Field Device Connected Online.")
    print(f"Broadcasting telemetry streams to server at {HOST}:{PORT}...\n")
    
    # Pre-defined field assets transmitting alternating protocol formats
    payloads = [
        "CSV:M02,23.8,78.4,NORMAL",
        "HEX:4d30312c32342e352c38322e31",  # Translates back to "M01,24.5,82.1"
        "CSV:M02,24.2,79.0,OVERHEAT",
        "HEX:4d30312c32352e302c38312e38"   # Translates back to "M01,25.0,81.8"
    ]
    
    try:
        while True:
            current_payload = random.choice(payloads)
            client_socket.sendto(current_payload.encode('utf-8'), (HOST, PORT))
            print(f"📤 Broadcasting Field Stream: {current_payload}")
            time.sleep(2.5)  # Pause briefly between intervals
    except KeyboardInterrupt:
        print("\n🛑 Simulator stream paused manually.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_simulator()