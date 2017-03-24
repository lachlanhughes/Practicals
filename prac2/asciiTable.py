

LOWER = 33
UPPER = 127

character = (input("Enter a character: "))
print("The ASCII code for {0} is {1}.".format(character, ord(character)))


try:
    number = int(input("Enter a number between {0} and {1}: ".format(LOWER, UPPER)))
    if LOWER <= number <= UPPER:
        print("The character for {0} is {1}.".format(number, chr(number)))
    else:
        print("The number must be between {0} and {1}.".format(LOWER, UPPER))
except ValueError:
    print("Must be a number!")



print("\n")
for i in range(LOWER, (UPPER+1), 1):
    print("{0:<3}{1:>6}".format(i, chr(i)))
