

file = open('name.txt', mode='r')
name = file.read()
print("Your name is {}.".format(name))
file.close()