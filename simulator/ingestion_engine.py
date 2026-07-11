"""
==========================================================
OmniNET-SCADA
Day 3 - Unified Telemetry Ingestion Engine
==========================================================

Purpose:
--------
This module receives raw telemetry from different field
devices and converts it into one standardized Python
dictionary.

Supported Protocols:
    • CSV
    • HEX (Hexadecimal encoded CSV)

Example Incoming Packets:

CSV:
CSV:M02,24.8,73.5,NORMAL

HEX:
HEX:4d30312c32332e342c37392e312c4e4f524d414c

Both become the same standardized JSON object.
"""

import binascii


def parse_csv_data(payload, protocol):
    """
    Converts a CSV payload into a standardized telemetry dictionary.

    Expected Format:
        DeviceID,Temperature,Humidity,Status

    Example:
        M02,24.3,74.1,NORMAL
    """

    try:

        parts = payload.strip().split(",")

        if len(parts) < 4:
            raise ValueError("Incomplete telemetry payload.")

        device_id = parts[0].strip()

        temperature = float(parts[1])

        humidity = float(parts[2])

        status = parts[3].strip()

        telemetry = {

            "device_id": device_id,

            "telemetry": {

                "temperature_c": temperature,

                "humidity_percent": humidity

            },

            "system_status": status,

            "layer_protocol": f"OmniNET-Normalized ({protocol})"

        }

        return telemetry

    except Exception as e:

        return {

            "error": f"CSV Parsing Error: {str(e)}"

        }


def parse_telemetry(raw_string):
    """
    Master Parsing Function.

    Automatically determines whether the incoming packet
    is CSV or HEX before sending it through the correct
    decoding pipeline.
    """

    try:

        raw_string = raw_string.strip()

        if raw_string == "":
            raise ValueError("Empty packet received.")

        ##################################################
        # CASE 1 : HEX PAYLOAD
        ##################################################

        if raw_string.startswith("HEX:"):

            hex_payload = raw_string[4:].strip()

            decoded_ascii = binascii.unhexlify(
                hex_payload
            ).decode("utf-8")

            return parse_csv_data(
                decoded_ascii,
                "HEX-Decoded"
            )

        ##################################################
        # CASE 2 : CSV PAYLOAD
        ##################################################

        elif raw_string.startswith("CSV:"):

            csv_payload = raw_string[4:].strip()

            return parse_csv_data(
                csv_payload,
                "CSV-Direct"
            )

        ##################################################
        # CASE 3 : LEGACY PAYLOAD
        ##################################################

        else:

            return parse_csv_data(
                raw_string,
                "Raw-Legacy"
            )

    except Exception as e:

        return {

            "error": f"Abstraction Pipeline Failure: {str(e)}"

        }


##############################################################
# Local Testing
##############################################################

if __name__ == "__main__":

    print("\n========== CSV TEST ==========\n")

    csv_sample = "CSV:M02,24.5,72.8,NORMAL"

    print(parse_telemetry(csv_sample))

    print("\n========== HEX TEST ==========\n")

    raw = "M01,25.3,74.1,NORMAL"

    hex_string = binascii.hexlify(
        raw.encode("utf-8")
    ).decode("utf-8")

    packet = "HEX:" + hex_string

    print(parse_telemetry(packet))