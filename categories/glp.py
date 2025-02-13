from base import TariffCategory


class GeneralLightingTariff(TariffCategory):
    """Handles bill calculation for General Lighting Purpose (GLP)."""

    def __init__(self):
        super().__init__("General Lighting Purpose (GLP)")

    def run(self):
        """Runs the billing calculation for the GLP category."""
        try:
            # Ask for the number of units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation
            if units_consumed <= 200:
                energy_charge = units_consumed * 4.10  # 410 Paisa = 4.10 Rs
            else:
                energy_charge = units_consumed * 4.80  # 480 Paisa = 4.80 Rs

            # Fixed charge calculation
            phase_choice = input(
                "Select Phase Type:\n1. Single Phase (₹30/month)\n2. Three Phase (₹70/month)\nEnter choice (1/2): "
            ).strip()
            if phase_choice == "1":
                fixed_charge = 30
            elif phase_choice == "2":
                fixed_charge = 70
            else:
                raise ValueError("Invalid phase choice. Please enter 1 or 2.")

            # Total bill calculation
            total_bill = fixed_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
