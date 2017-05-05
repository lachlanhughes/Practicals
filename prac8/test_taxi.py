from prac8.taxi import Car,Taxi,UnreliableCar,SilverServiceTaxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print("Current fare = ${}\n".format(taxi.get_fare()))

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Current fare = ${}\n".format(taxi.get_fare()))

    corolla = UnreliableCar("corolla", 100, 50)
    corolla.drive(100)
    print(corolla)
    print("")

    hummer = SilverServiceTaxi("hummer", 200, 2)
    hummer.drive(10)
    print(hummer)
    print("Current fare = ${}\n".format(hummer.get_fare()))

main()