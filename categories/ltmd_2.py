from base import TariffCategory


class LTMD2Tariff(TariffCategory):
    """Handles bill calculation for LTMD 2: Commercial/Industrial Purpose (Above 15 KW)."""

    def __init__(self):
        super().__init__("LTMD 2 - Commercial/Industrial Purpose (Above 15 KW)")

    def run(self):
        """Runs the billing calculation for the LTMD 2 category."""
        try:
            # Ask for contract demand (in kW)
            contract_demand = float(input("Enter Contract Demand (in kW): "))
            if contract_demand <= 0:
                raise ValueError("Contract Demand must be greater than 0.")

            # Ask for maximum demand recorded (in kW)
            max_demand = float(
                input("Enter Maximum Demand recorded in the month (in kW): ")
            )
            if max_demand <= 0:
                raise ValueError("Maximum Demand must be greater than 0.")

            # Calculate billing demand (highest among max demand, 85% of contract demand, or 6 kW)
            billing_demand = max(max_demand, 0.85 * contract_demand, 6)
            print(f"Billing Demand: {billing_demand:.2f} kW")

            # Ask for energy consumption (in units)
            units_consumed = int(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                raise ValueError("Units consumed cannot be negative.")

            # Energy charge calculation
            if billing_demand <= 50:
                energy_charge = units_consumed * 4.80  # 480 Paisa = 4.80 Rs
            else:
                energy_charge = units_consumed * 5.00  # 500 Paisa = 5.00 Rs

            # Fixed charge calculation based on billing demand
            fixed_charge = 0
            if billing_demand <= 50:
                fixed_charge = billing_demand * 175  # ₹175 per kW
            elif billing_demand <= 80:
                fixed_charge = (50 * 175) + (
                    (billing_demand - 50) * 230
                )  # ₹175 for first 50 kW, ₹230 for next 30 kW
            else:
                fixed_charge = (
                    (50 * 175) + (30 * 230) + ((billing_demand - 80) * 300)
                )  # ₹300 for demand above 80 kW

            # Excess Demand Charge (if billing demand exceeds contract demand)
            excess_demand_charge = 0
            if billing_demand > contract_demand:
                excess_demand_charge = (
                    billing_demand - contract_demand
                ) * 425  # ₹425 per kW for excess demand

            # Ask for power factor percentage
            power_factor = float(
                input("Enter Power Factor Percentage (e.g., 95 for 95%): ")
            )
            if power_factor <= 0 or power_factor > 100:
                raise ValueError("Power Factor should be between 0 and 100.")

            # Power Factor adjustment calculation
            power_factor_adjustment = 0
            if 90 <= power_factor <= 95:
                power_factor_adjustment = (power_factor - 90) * 0.15 * units_consumed
            elif power_factor > 95:
                power_factor_adjustment = (
                    (95 - 90) * 0.15 + (power_factor - 95) * 0.27
                ) * units_consumed
            elif power_factor < 90:
                power_factor_adjustment = (
                    (90 - power_factor) * 3 * units_consumed * -1
                )  # Negative adjustment

            # Total bill calculation
            total_bill = (
                energy_charge
                + fixed_charge
                + excess_demand_charge
                + power_factor_adjustment
            )
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
