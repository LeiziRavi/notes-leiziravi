def taxiFare(distanceInKm, base_fare=4.00, var_fare=0.25):
    total_fare = base_fare + (var_fare * (distanceInKm * 1000/140))

    return total_fare


def main():
    distanceTravelled = float(input("Enter distance travelled in km: "))
    print("Taxi fare for ", distanceTravelled,
          "km is $", format(taxiFare(distanceTravelled), ".2f"))


main()
