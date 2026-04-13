import subprocess
import re

def link_test(interface):
    print(f"[LINK] Testing {interface}")

    result = subprocess.run(
        ["ethtool", interface],
        capture_output=True,
        text=True
    )

    output = result.stdout

    def extract(field):
        match = re.search(rf"{field}:\s*(.+)", output)
        return match.group(1).strip() if match else None

    speed = extract("Speed")
    duplex = extract("Duplex")

    link_detected = bool(
        re.search(r"Link detected:\s*yes", output, re.IGNORECASE)
    )

    # 🔥 SMART FIX: handle VM / missing PHY data
    if speed and "unknown" in speed.lower():
        speed = None

    if duplex and "half" in duplex.lower() and "auto-negotiation: off" in output:
        duplex = "Unknown (forced or virtual NIC)"

    data = {
        "interface": interface,
        "speed": speed,
        "duplex": duplex,
        "link_detected": link_detected,
        "note": "virtual_or_limited_driver_possible"
    }

    print("[LINK]", data)
    return data
