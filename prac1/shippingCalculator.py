items = 0
total = 0
price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))


for i in range(0, number_of_items, 1):
    price = price + int(input("Price of item {:.2f}: $".format(i + 1)))



if price > 100:
    price = price * 0.9

print("Total price for {:.2f} items is ${:.2f}".format(number_of_items, price))