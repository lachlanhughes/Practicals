

file = open('numbers.txt', mode='r')
number = 0
for i in file:
    number += int(i)
print(number)
file.close()