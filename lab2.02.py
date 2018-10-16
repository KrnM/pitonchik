fileA = open('C:\\Users\\ACER\\Documents\\GitHub\\pitonchik\\a.txt')
lines = fileA.readlines()
list1 = []
dictionary = {}
for line in lines:
    for word in line.split():
        word = word.lower()
        list1.append(word)

for i in list1:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

import xml.etree.cElementTree as ET

root = ET.Element("root")
words = ET.SubElement(root, "words")

for i in dictionary:
    print("'%s':%s" % (i, dictionary[i]))
    ET.SubElement(words, i, quantity=str(dictionary[i]))

tree = ET.ElementTree(root)
tree.write("C:\\Users\\ACER\\Documents\\GitHub\\pitonchik\\filename.xml", encoding='utf-8')