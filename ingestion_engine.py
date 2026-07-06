import json
from datetime import datetime

class OmniNetIngestionEngine:
    """
    Standardizes inconsistent data streams from multiple manufacturers
    into a unified, universally readable telemetry format.
    """
    
    @staticmethod
    def parse_manufacturer_a(hex_packet):
        """
        Manufacturer A sends data in a Hexadecimal format to save bandwidth.
        Format: [2 chars DeviceID][4 chars Voltage x10][4 chars Current x100]
        Example: "0108fc01f4" -> Device 01, 230.0V, 5.00A
        """
        try:
            device_id = str(int(hex_packet[0:2], 16))
            voltage = int(hex_packet[2:6], 16) / 10.0
            current = int(hex_packet[6:10], 16) / 100.0
            
            return {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "device_id": f"OMNI-A-{device_id.zfill(3)}",
                "metrics": {
                    "voltage_v": voltage,
                    "current_a": current,
                    "power_w": round(voltage * current, 2)
                },
                "status": "ONLINE"
            }
        except Exception as e:
            return {"error": f"Failed to parse Manufacturer A payload: {str(e)}"}

    @staticmethod
    def parse_manufacturer_b(csv_packet):
        """
        Manufacturer B passes data in a simple human-readable CSV string.
        Format: "DeviceID,Voltage,Current,Status"
        Example: "DEV-99,228.5,4.85,OK"
        """
        try:
            parts = csv_packet.split(',')
            device_id = parts[0].strip()
            voltage = float(parts[1])
            current = float(parts[2])
            status = "ONLINE" if parts[3].strip() == "OK" else "FAULT"
            
            return {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "device_id": f"OMNI-B-{device_id}",
                "metrics": {
                    "voltage_v": voltage,
                    "current_a": current,
                    "power_w": round(voltage * current, 2)
                },
                "status": status
            }
        except Exception as e:
            return {"error": f"Failed to parse Manufacturer B payload: {str(e)}"}


# --- Local Test Execution ---
if __name__ == "__main__":
    print("--- OmniNET SCADA: Protocol Ingestion Test --- \n")
    engine = OmniNetIngestionEngine()
    
    # Simulating raw streams coming from different factory field hardware
    raw_payload_a = "0108fc01f4"  # Hex data
    raw_payload_b = "DEV-99,228.5,4.85,OK"  # CSV data
    
    # Normalize data structures cleanly through our abstraction layer
    normalized_a = engine.parse_manufacturer_a(raw_payload_a)
    normalized_b = engine.parse_manufacturer_b(raw_payload_b)
    
    print("[1] Manufacturer A Normalized Payload:")
    print(json.dumps(normalized_a, indent=4))
    print("\n[2] Manufacturer B Normalized Payload:")
    print(json.dumps(normalized_b, indent=4))