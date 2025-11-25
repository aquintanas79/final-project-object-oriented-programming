class Monitor:
    """
    CRC Card: Monitor
    Responsibility: Display table results, real-time variations.
    """
    def update_table(self, components):
        print("\n[MONITOR] Real-Time Values:")
        print(f"{'Name':<15} | {'Voltage (V)':<10} | {'Current (A)':<10}")
        print("-" * 45)
        for comp in components:
            print(f"{comp.name:<15} | {comp.voltage:<10.2f} | {comp.current:<10.4f}")