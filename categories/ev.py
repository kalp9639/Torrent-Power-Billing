from base import TariffCategory

class ElectricVehicleChargingStationTariff(TariffCategory):
    """Handles bill calculation for EV: HT Electric Vehicle Charging Stations."""

    def __init__(self):
        super().__init__("EV - HT Electric Vehicle Charging Stations")

    def run(self):
        """Runs the billing calculation for the EV category."""
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
            energy_charge = units_consumed * 4.10  # 410 Paisa = 4.10 Rs per unit

            # Demand charge calculation
            if billing_demand <= contract_demand:
                demand_charge = billing_demand * 25  # Rs. 25 per kW/month for demand up to contract demand
            else:
                demand_charge = (contract_demand * 25) + ((billing_demand - contract_demand) * 50)  # Rs. 50 per kW/month for excess demand

            # Total bill calculation
            total_bill = demand_charge + energy_charge
            print(f"Total Bill Amount: ₹{total_bill:.2f}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
