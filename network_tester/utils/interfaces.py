import subprocess

def get_all():
    result = subprocess.run(
        ["ip", "-o", "link", "show"],
        capture_output=True,
        text=True
    )

    interfaces = []
    for line in result.stdout.splitlines():
        name = line.split(":")[1].strip()
        if name != "lo":
            interfaces.append(name)

    return interfaces


def is_up(interface):
    res = subprocess.run(
        ["ip", "link", "show", interface],
        capture_output=True,
        text=True
    )
    return "state UP" in res.stdout


def has_link(interface):
    res = subprocess.run(
        ["ethtool", interface],
        capture_output=True,
        text=True
    )
    return "Link detected: yes" in res.stdout


def select_ethernet():
    for iface in get_all():
        if iface.startswith("eth") and is_up(iface) and has_link(iface):
            return iface
    return None
