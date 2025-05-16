file= open('Codingal.txt2', 'r')
print(file.read())
file.close()

file = open('Codingal.txt2', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt2' , 'a')
file.write("Hi ! I am Sheep and I am 2 yr old.")
file.close()