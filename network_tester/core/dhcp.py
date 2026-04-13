import subprocess
import shutil

def dhcp_test(interface):
    print(f"[DHCP] Testing interface: {interface}")

    # check dependency
    if not shutil.which("dhclient"):
        return {
            "interface": interface,
            "success": False,
            "error": "dhclient not installed"
        }

    subprocess.run(["dhclient", "-r", interface],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    result = subprocess.run(
        ["dhclient", "-v", interface],
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr

    success = "bound to" in output.lower()

    print("[DHCP]", "SUCCESS" if success else "FAILED")

    return {
        "interface": interface,
        "success": success,
        "raw_output": output
    }
