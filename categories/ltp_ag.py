from base import TariffCategory

class AgriculturalTariff(TariffCategory):
    """Handles bill calculation for LTP (AG): Agricultural Purpose."""

    def __init__(self):
        super().__init__("LTP (AG) - Agricultural Purpose")

    def run(self):
        """Runs the billing calculation for the Agricultural category."""
        try:
            # Ask for the number of units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (Flat Rate)
            energy_charge = units_consumed * 3.40  # 340 Paisa = 3.40 Rs

            # Ask for the connected BHP (Brake Horse Power)
            bhp = float(input("Enter the connected load in BHP: "))
            if bhp <= 0:
                raise ValueError("BHP must be greater than 0.")

            # Minimum charge calculation
            minimum_charge = bhp * 10  # 10 Rs per BHP

            # Total bill calculation
            total_bill = energy_charge + minimum_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
