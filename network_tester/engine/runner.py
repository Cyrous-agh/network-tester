from network_tester.utils.interfaces import get_all, select_ethernet

def run_all():
    all_ifaces = get_all()
    eth = select_ethernet()

    print("All interfaces:", all_ifaces)
    print("Selected ethernet:", eth)

    return {
        "all_interfaces": all_ifaces,
        "selected_ethernet": eth
    }
