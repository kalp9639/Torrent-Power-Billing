from base import TariffCategory

class HighTensionAMCPumpingStationsTariff(TariffCategory):
    """Handles bill calculation for HTMD-2: High Tension AMC Pumping Stations."""

    def __init__(self):
        super().__init__("HTMD-2 - High Tension AMC Pumping Stations")

    def run(self):
        """Runs the billing calculation for the HTMD-2 category."""
        try:
            # Ask for the billing demand (in kW)
            billing_demand = float(input("Enter the billing demand (in kW): "))
            if billing_demand <= 0:
                raise ValueError("Billing demand must be greater than zero.")

            # Ask for units consumed
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation (flat rate)
            energy_charge = units_consumed * 4.10  # 410 Paisa = 4.10 Rs per unit

            # Fixed charge calculation
            fixed_charge = billing_demand * 225  # Rs. 225 per kW

            # Excess demand charge (if applicable)
            excess_demand = max(0, billing_demand - 100)  # Assuming 100 kW as contract demand
            excess_charge = excess_demand * 285  # Rs. 285 per kW

            # TOU charge (flat rate)
            tou_charge = units_consumed * 0.60  # 60 Paisa/unit

            # Night Time Charge (2200 to 0600 hrs) - Flat 30 Paisa/unit
            night_units = int(input("Enter the number of units consumed during Night Time (2200 Hrs to 0600 Hrs): "))
            night_time_charge = night_units * 0.30  # 30 Paisa/unit

            # Power Factor Charge
            power_factor = float(input("Enter the power factor (%): "))
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
