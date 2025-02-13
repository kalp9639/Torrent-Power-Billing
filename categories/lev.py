from base import TariffCategory


class ElectricVehicleChargingTariff(TariffCategory):
    """Handles bill calculation for LEV: LT - Electric Vehicle Charging Stations."""

    def __init__(self):
        super().__init__("LEV - LT Electric Vehicle Charging Stations")

    def run(self):
        """Runs the billing calculation for the LEV category."""
        try:
            # Ask for energy consumption (in units)
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (Flat Rate)
            energy_charge = units_consumed * 4.20  # 420 Paisa = 4.20 Rs

            # Fixed charge calculation
            fixed_charge = 25  # Rs. 25 per month per installation

            # Total bill calculation
            total_bill = fixed_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
