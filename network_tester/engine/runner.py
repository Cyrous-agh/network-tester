from network_tester.utils.interfaces import get_all, select_best_interface
from network_tester.core.dhcp import dhcp_test
from network_tester.core.link import link_test

def run_all():
    all_ifaces = get_all()
    eth = select_best_interface()

    print("\n=== NETWORK TESTER ===")
    print("All interfaces:", all_ifaces)
    print("Selected ethernet:", eth)

    dhcp_result = None

    if eth:
        dhcp_result = dhcp_test(eth)
    else:
        print("[DHCP] No ethernet interface found!")

    link_result = None

    if eth:
        link_result = link_test(eth)

    return {
        "all_interfaces": all_ifaces,
        "selected_ethernet": eth,
        "dhcp": dhcp_result,
        "link": link_result,
    }
