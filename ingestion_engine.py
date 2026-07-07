import json

def parse_hex_payload(hex_str):
    try:
        # Convert hexadecimal string back to regular text
        decoded_text = bytes.fromhex(hex_str).decode('utf-8')
        return parse_csv_payload(decoded_text)
    except Exception as e:
        print(f"⚠️ Error parsing HEX data: {e}")
        return None

def parse_csv_payload(csv_str):
    try:
        # Expected CSV structure: DeviceID, Temperature, Humidity, Status
        parts = csv_str.strip().split(',')
        if len(parts) >= 4:
            return {
                "device_id": parts[0],
                "telemetry": {
                    "temperature_c": float(parts[1]),
                    "humidity_percent": float(parts[2])
                },
                "system_status": parts[3],
                "layer_protocol": "OmniNET-Normalized"
            }
    except Exception as e:
        print(f"⚠️ Error parsing CSV data: {e}")
    return None

if __name__ == "__main__":
    # Local self-test
    print("Testing parser functions locally...")
    sample_csv = "M02,23.8,78.4,NORMAL"
    print(parse_csv_payload(sample_csv))