from base import TariffCategory

class ResidentialTariff(TariffCategory):
    """Handles bill calculation for Residential General Purpose (RGP) and Below Poverty Line (BPL)."""

    def __init__(self):
        super().__init__("Residential Purpose (RGP)")

    def run(self):
        """Runs the billing calculation for the RGP category."""
        try:
            # Ask user to select RGP or BPL
            user_type = input("Choose Residential Type: \n1. RGP (General)\n2. BPL (Below Poverty Line)\nEnter choice (1/2): ").strip()

            if user_type not in ['1', '2']:
                raise ValueError("Invalid choice. Please enter 1 or 2.")

            # Ask for the number of units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation
            if user_type == '1':  # RGP General
                if units_consumed <= 50:
                    energy_charge = units_consumed * 3.2  # 320 Paisa = 3.2 Rs
                elif units_consumed <= 200:
                    energy_charge = units_consumed * 3.95
                else:
                    energy_charge = units_consumed * 5.0
            else:  # BPL
                if units_consumed <= 50:
                    energy_charge = units_consumed * 1.5  # 150 Paisa = 1.5 Rs
                elif units_consumed <= 200:
                    energy_charge = units_consumed * 3.95
                else:
                    energy_charge = units_consumed * 5.0

            # Fixed charge calculation
            if user_type == '1':  # RGP General
                phase_choice = input("Select Phase Type:\n1. Single Phase (₹25/month)\n2. Three Phase (₹65/month)\nEnter choice (1/2): ").strip()
                if phase_choice == '1':
                    fixed_charge = 25
                elif phase_choice == '2':
                    fixed_charge = 65
                else:
                    raise ValueError("Invalid phase choice. Please enter 1 or 2.")
            else:  # BPL
                fixed_charge = 5  # Flat charge

            # Total bill calculation
            total_bill = fixed_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
