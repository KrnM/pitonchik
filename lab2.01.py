fileA = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\a.txt')
lines = fileA.readlines()
fileA.close()

i = 0
fileA = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\a.txt')
fileB1 = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\b1.txt', 'w')
fileB2 = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\b2.txt', 'w')
for line in lines:
    i += 1
    if i % 2 == 0:
        line = line.upper()
        fileB1.write(line)
    elif (i - 1) % 2 == 0:
        line = line.lower()
        fileB2.write(line)

fileA.close()
fileB1.close()
fileB2.close()

fileB1 = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\b1.txt')
print(fileB1.read())
fileB2 = open('C:\\Users\\ACER\\PycharmProjects\\lab2.01\\b2.txt')
print(fileB2.read())