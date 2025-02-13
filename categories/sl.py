from base import TariffCategory

class StreetLightTariff(TariffCategory):
    """Handles bill calculation for SL: Street Light category."""

    def __init__(self):
        super().__init__("SL - Street Light")

    def run(self):
        """Runs the billing calculation for the SL category."""
        try:
            # Ask for energy consumption (in units)
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (Flat Rate)
            energy_charge = units_consumed * 4.30  # 430 Paisa = 4.30 Rs

            # Total bill calculation
            total_bill = energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
