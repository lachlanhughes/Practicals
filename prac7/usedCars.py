from prac7.car import Car


def main():
    bus = Car("bus", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)



    limo = Car("limo", 100)
    limo.add_fuel(20)
    print("\nfuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)

    print("\n")
    print(limo)


main()
