

def main():
    name = get_name()
    frequency = int(input("Choose how often to repeat letters: "))
    loop_name(name, frequency)


def get_name():
    name = input("Enter your name: ")
    while not name:
        print("Name cannot be blank")
        name = input("Enter your name: ")
    return name


def loop_name(name, frequency):
    for i in range(len(name)):
        if i % frequency == 0:
            print(name[i])


main()