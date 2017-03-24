

numbers = []


print("Please enter five numbers:")
numbers += [int(input("Number one: "))]
numbers += [int(input("Number two: "))]
numbers += [int(input("Number three: "))]
numbers += [int(input("Number four: "))]
numbers += [int(input("Number five: "))]

print("\nThe first number is {}".format(numbers[0]))
print("The last number is {0}".format(numbers[-1]))
print("The smallest number is {0}".format(min(numbers)))
print("The largest number is {0}".format(max(numbers)))
print("The average of the numbers is {0}".format(sum(numbers)/len(numbers)))