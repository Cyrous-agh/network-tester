from network_tester.engine.runner import run_all

def main():
    print("=== Network Tester Started ===")
    results = run_all()
    print("Results:", results)

if __name__ == "__main__":
    main()
