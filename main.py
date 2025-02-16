import importlib
from categories.rgp import ResidentialTariff
from categories.glp import GeneralLightingTariff
from categories.nonrgp import NonResidentialTariff
from categories.ltp_ag import AgriculturalTariff
from categories.ltmd_1 import LTMD1Tariff
from categories.ltmd_2 import LTMD2Tariff
from categories.sl import StreetLightTariff
from categories.ev import ElectricVehicleChargingStationTariff
from categories.tmp import TemporarySupplyTariff
from categories.htmd_1 import HighTensionLoadTariff
from categories.htmd_2 import HighTensionAMCPumpingStationsTariff
from categories.htmd_3 import TemporarySupplyHighTensionTariff
from categories.lev import ElectricVehicleChargingTariff
from categories.htmd_metro import MetroTractionTariff


def main():
    # Available tariff categories with module and class names
    categories = {
        "1": ResidentialTariff(),
        "2": GeneralLightingTariff(),
        "3": NonResidentialTariff(),
        "4": AgriculturalTariff(),
        "5": LTMD1Tariff(),
        "6": LTMD2Tariff(),
        "7": StreetLightTariff(),
        "8": ElectricVehicleChargingTariff(),
        "9": TemporarySupplyTariff(),
        "10": HighTensionLoadTariff(),
        "11": HighTensionAMCPumpingStationsTariff(),
        "12": TemporarySupplyHighTensionTariff(),
        "13": ElectricVehicleChargingStationTariff(),
        "14": MetroTractionTariff()
    }

    print("Choose Tariff Category:")

    try:    
        for key, tariff_class in categories.items():
            tariff_instance = tariff_class  # Instantiate the class
            print(f"{key}. {tariff_instance.name}")  # Display the category name
    except Exception as e:
        print(f"Error loading category: {e}")

    # Get user choice
    choice = input("Enter choice (1-14): ").strip()

    if categories.get(choice):
        categories.get(choice).run()
    else:
        print("Invalid choice")  


if __name__ == "__main__":
    main()
