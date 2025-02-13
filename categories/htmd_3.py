from base import TariffCategory


class TemporarySupplyHighTensionTariff(TariffCategory):
    """Handles bill calculation for HTMD-3: Temporary Supply (100 kW & Above)."""

    def __init__(self):
        super().__init__("HTMD-3 - Temporary Supply (100 kW & Above)")

    def run(self):
        """Runs the billing calculation for the HTMD-3 category."""
        try:
            # Ask for the billing demand (in kW)
            billing_demand = float(input("Enter the billing demand (in kW): "))
            if billing_demand <= 0:
                raise ValueError("Billing demand must be greater than zero.")

            # Ask for the contract demand (in kW)
            contract_demand = float(input("Enter the contract demand (in kW): "))
            if contract_demand <= 0:
                raise ValueError("Contract demand must be greater than zero.")

            # Ask for units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (flat rate)
            energy_charge = units_consumed * 7.05  # 705 Paisa = 7.05 Rs per unit

            # Fixed charge calculation based on contract demand
            if billing_demand <= contract_demand:
                fixed_charge = billing_demand * 25  # Rs. 25 per kW/day
            else:
                fixed_charge = (contract_demand * 25) + (
                    (billing_demand - contract_demand) * 30
                )  # Rs. 30 per kW/day for excess

            # TOU charge (flat rate)
            tou_charge = units_consumed * 0.60  # 60 Paisa/unit

            # Power Factor Charge
            power_factor = float(input("Enter the power factor (%): "))
            power_factor_charge = 0
            if power_factor < 90:
                power_factor_charge = (
                    90 - power_factor
                ) * 3  # 3 Paisa/unit for each 1% below 90%
            elif power_factor <= 95:
                power_factor_charge = (
                    95 - power_factor
                ) * 0.15  # 0.15 Paisa/unit for each 1% improvement from 90% to 95%
            else:
                power_factor_charge = (
                    power_factor - 95
                ) * 0.27  # 0.27 Paisa/unit for each 1% improvement above 95%

            # Total bill calculation
            total_bill = fixed_charge + energy_charge + tou_charge + power_factor_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
