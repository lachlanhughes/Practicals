
name = input("Enter your name: ")

file = open('name.txt', mode='w')
file.write(name)
file.close()