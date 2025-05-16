#open the file in read mode
file_read  = open('Codingal.txt2', 'r')
print("File in Read mode-")
print(file_read.read())
file_read.close()


#open the file in write mode
file_write = open('Codingal.txt2' , 'w')
#write in the file
file_write.write("File in write mode....")
file_write.write("HI! I am a Sheep. I am 2 yr old.")
file_write.close()

#open the file in append mode
file_append = open('Codingal.txt2', 'a')
#append in the file
file_append.write("\n File in append mode...")
file_append.write("Hi ! I am Sheep. I am 2 yrs old")
file_write.close()

