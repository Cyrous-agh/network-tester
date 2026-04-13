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


def get_details(interface):
    result = subprocess.run(
        ["ip", "a", "show", interface],
        capture_output=True,
        text=True
    )
    return result.stdout


def is_up(interface):
    out = get_details(interface)
    return "state UP" in out or "LOWER_UP" in out


def has_carrier(interface):
    out = get_details(interface)
    return "NO-CARRIER" not in out


def has_ip(interface):
    out = get_details(interface)
    return "inet " in out


def select_best_interface():
    candidates = []

    for iface in get_all():

        if iface == "lo":
            continue

        up = is_up(iface)
        carrier = has_carrier(iface)
        ip = has_ip(iface)

        score = 0
        if up: score += 1
        if carrier: score += 2
        if ip: score += 3

        candidates.append((iface, score))

    # sort by best score
    candidates.sort(key=lambda x: x[1], reverse=True)

    best = candidates[0][0] if candidates else None

    return best
