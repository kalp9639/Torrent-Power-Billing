from base import TariffCategory


# this is a comment
class MetroTractionTariff(TariffCategory):
    """Handles bill calculation for HTMD - Metro Traction."""

    def __init__(self):
        super().__init__("HTMD - Metro Traction")

    def run(self):
        """Runs the billing calculation for the Metro Traction category."""
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
            energy_charge = units_consumed * 3.55  # 355 Paisa = 3.55 Rs per unit

            # Demand charge calculation
            if billing_demand <= contract_demand:
                demand_charge = (
                    billing_demand * 335
                )  # Rs. 335 per kW/month for demand up to contract demand
            else:
                demand_charge = (contract_demand * 335) + (
                    (billing_demand - contract_demand) * 385
                )  # Rs. 385 per kW/month for excess demand

            # Power Factor rebate/penalty calculation
            power_factor = float(input("Enter the power factor percentage: "))
            if power_factor < 0 or power_factor > 100:
                raise ValueError("Power factor should be between 0 and 100.")

            rebate_or_penalty = 0
            if 90 <= power_factor <= 95:
                rebate_or_penalty = (
                    95 - power_factor
                ) * 0.15  # Rebate for improvement from 90% to 95%
            elif power_factor > 95:
                rebate_or_penalty = (
                    power_factor - 95
                ) * 0.27  # Rebate for improvement above 95%
            elif power_factor < 90:
                rebate_or_penalty = (
                    90 - power_factor
                ) * 3  # Penalty for decrease below 90%

            # TOU charge calculation (flat rate)
            tou_charge = units_consumed * 0.60  # 60 Paisa = 0.60 Rs per unit

            # Night Time charge calculation
            night_time_charge = (
                units_consumed * 0.30
            )  # 30 Paisa = 0.30 Rs per unit for Night Time

            # Total bill calculation
            total_bill = (
                demand_charge
                + energy_charge
                + tou_charge
                + night_time_charge
                - rebate_or_penalty
            )
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
