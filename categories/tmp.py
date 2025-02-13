from base import TariffCategory

class TemporarySupplyTariff(TariffCategory):
    """Handles bill calculation for TMP: Temporary Supply (Below 100 kW)."""

    def __init__(self):
        super().__init__("TMP - Temporary Supply (Below 100 kW)")

    def run(self):
        """Runs the billing calculation for the TMP category."""
        try:
            # Ask for energy consumption (in units)
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (Flat Rate)
            energy_charge = units_consumed * 5.10  # 510 Paisa = 5.10 Rs

            # Ask for the number of days the temporary supply was used
            days_used = int(input("Enter the number of days temporary supply was used: "))
            if days_used < 0:
                raise ValueError("Days used cannot be negative.")

            # Fixed charge calculation (₹25/kW/day)
            fixed_charge = days_used * 25  # Rs. 25 per kW per day

            # Total bill calculation
            total_bill = fixed_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
