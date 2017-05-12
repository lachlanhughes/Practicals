from prac8.taxi import Car, Taxi, SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    #menu = "Bill to date: ${:.2f}\nq)uit, c)hoose taxi, d)rive\n>>> ".format(bill)

    selection = input("Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>> ")
    while selection != "q":
        if selection == "c":
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i,taxi))
            taxi_selection = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_selection]
        elif selection == "d":
            distance_to_drive = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            bill += trip_cost
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
        else:
            print("Please enter a valid option")
        selection = input("Bill to date: ${:.2f}\nq)uit, c)hoose taxi, d)rive\n>>> ".format(bill))


main()
