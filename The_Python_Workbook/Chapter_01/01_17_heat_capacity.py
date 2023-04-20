SPEC_HEAT = 4.186
JOULES_TO_KWH = 2.7778e-7

mass_of_water = float(input("Enter Mass of water (in gms): "))
temp_change = float(input("Enter change of temperature (in degree C): "))


amnt_of_energy = mass_of_water * SPEC_HEAT * temp_change
print(f"{amnt_of_energy:.2f} J is required to increase/decrease {temp_change:.2f} degree C temperature of {mass_of_water:.2f} gms of water.")



cost = amnt_of_energy * JOULES_TO_KWH * 8.9
print(f"Cost of heating {mass_of_water:.2f} gms of water  in an hour is {cost:.3f} cents")