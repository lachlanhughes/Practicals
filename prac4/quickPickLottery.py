
import random


rows = int(input("How many quick picks? "))

for i in range(0,rows):
    row = [random.randint(1, 45)]
    while len(row) < 6:
        number = random.randint(1, 45)
        if not(number in row):
            row += [number]
    row = sorted(row)

    print("{0:>2} {1:>2} {2:>2} {3:>2} {4:>2} {5:>2}".format(*row))





#for i in range(0, rows):
#    row = [random.randint(1, 45), random.randint(1, 45), random.randint(1, 45), random.randint(1, 45), random.randint(1, 45), random.randint(1, 45)]
#    print("{0:>2} {1} {2} {3} {4} {5}".format(min(row), ))