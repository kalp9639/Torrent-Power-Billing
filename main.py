import importlib


def main():
    # Available tariff categories
    categories = {
        "1": "rgp.ResidentialTariff",
        "2": "glp.GeneralLightingTariff",
        "3": "nonrgp.NonResidentialTariff",
        "4": "ltp_ag.AgriculturalTariff",
        "5": "ltmd_1.LTMD1Tariff",
        "6": "ltmd_2.LTMD2Tariff",
        "7": "sl.StreetLightTariff",
        "8": "lev.ElectricVehicleChargingTariff",
        "9": "tmp.TemporarySupplyTariff",
        "10": "htmd_1.HighTensionLoadTariff",
        "11": "htmd_2.HighTensionAMCPumpingStationsTariff",
        "12": "htmd_3.TemporarySupplyHighTensionTariff",
        "13": "ev.ElectricVehicleChargingStationTariff",
        "14": "htmd_metro.MetroTractionTariff"
    }

    print("Choose Tariff Category:")
    for key, value in categories.items():
        print(f"{key}. {value.split('.')[-1]}")

    choice = input("Enter choice (1-14): ").strip()

    # Check if the user input is valid
    if choice in categories:
        category_path = categories[choice]
        module_name, class_name = category_path.rsplit(".", 1)

        # Dynamically import the module and class
        module = importlib.import_module(f"categories.{module_name}")
        tariff_class = getattr(module, class_name)

        # Instantiate the tariff class and run the calculation
        tariff = tariff_class()
        tariff.run()
    else:
        print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()
