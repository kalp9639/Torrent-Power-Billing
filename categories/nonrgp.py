from base import TariffCategory


class NonResidentialTariff(TariffCategory):
    """Handles bill calculation for Non-RGP: Commercial and Industrial Purpose (Up to & Including 15 KW)."""

    def __init__(self):
        super().__init__("Non-RGP (Commercial and Industrial)")

    def run(self):
        """Runs the billing calculation for the Non-RGP category."""
        try:
            # Ask for the number of units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (Flat Rate)
            energy_charge = units_consumed * 4.60  # 460 Paisa = 4.60 Rs

            # Ask for the connected load (KW)
            load_kw = float(input("Enter the connected load in KW (Up to 15KW): "))
            if load_kw <= 0 or load_kw > 15:
                raise ValueError("Invalid load. Must be between 0 and 15 KW.")

            # Fixed charge calculation
            if load_kw <= 5:
                fixed_charge = load_kw * 70  # 70 Rs per kW
            else:
                fixed_charge = load_kw * 90  # 90 Rs per kW

            # Total bill calculation
            total_bill = fixed_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
