from base import TariffCategory

class HighTensionLoadTariff(TariffCategory):
    """Handles bill calculation for HTMD-1: High Tension Load (100 kW & Above)."""

    def __init__(self):
        super().__init__("HTMD-1 - High Tension Load (100 kW & Above)")

    def run(self):
        """Runs the billing calculation for the HTMD-1 category."""
        try:
            # Ask for the billing demand (in kW)
            billing_demand = float(input("Enter the billing demand (in kW): "))
            if billing_demand <= 0:
                raise ValueError("Billing demand must be greater than zero.")

            # Determine the highest demand value
            max_demand = max(billing_demand, 0.85 * billing_demand, 100)
            print(f"Billing Demand: {max_demand:.2f} kW")

            # Ask for units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation
            if units_consumed <= 400 * max_demand:
                energy_charge = units_consumed * 4.55  # 455 Paisa = 4.55 Rs per unit
            else:
                energy_charge = 400 * max_demand * 4.55 + (units_consumed - 400 * max_demand) * 4.45  # 445 Paisa = 4.45 Rs per unit

            # Fixed charge calculation
            if max_demand <= 1000:
                fixed_charge = max_demand * 260  # Rs. 260 per kW
            else:
                fixed_charge = max_demand * 335  # Rs. 335 per kW

            # Excess demand charge (if applicable)
            excess_demand = max_demand - billing_demand
            excess_charge = 0
            if excess_demand > 0:
                excess_charge = excess_demand * 385  # Rs. 385 per kW

            # TOU charge calculation
            tou_charge = 0
            if max_demand <= 300:
                tou_charge = units_consumed * 0.80  # 80 Paisa/unit
            else:
                tou_charge = units_consumed * 1.00  # 100 Paisa/unit

            # Night Time Charge (2200 to 0600 hrs) - Flat 30 Paisa/unit
            night_units = int(input("Enter the number of units consumed during Night Time (2200 Hrs to 0600 Hrs): "))
            night_time_charge = night_units * 0.30  # 30 Paisa/unit

            # Power Factor Charge
            power_factor = float(input("Enter Power Factor Percentage (e.g., 95 for 95%): "))
            power_factor_charge = 0
            if power_factor < 90:
                power_factor_charge = (90 - power_factor) * 3  # 3 Paisa/unit for each 1% below 90%
            elif power_factor <= 95:
                power_factor_charge = (95 - power_factor) * 0.15  # 0.15 Paisa/unit for each 1% improvement from 90% to 95%
            else:
                power_factor_charge = (power_factor - 95) * 0.27  # 0.27 Paisa/unit for each 1% improvement above 95%

            # Total bill calculation
            total_bill = fixed_charge + energy_charge + excess_charge + tou_charge + night_time_charge + power_factor_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
