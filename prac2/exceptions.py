try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# When will a ValueError occur?

# When numerator or denominator are not valid number (eg. letters).


# When will a ZeroDivisionError occur?

# When the denominator is set to 0.


# Could you change the code to avoid the possibility of a ZeroDivisionError?

# Have the program check for zeroes before trying to divide and re-prompting the user.