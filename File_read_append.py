
File1= open('Output.txt','w')
a=input("Enter test to write to the file: ")
print("Data Successfully written to Output.txt.")

File_write=File1.write(a)
File1.close()

File1=open('Output.txt','a')
b=input("Enter additional text to append: ")
print("Data successfully appended.")
File_nextline= File1.write("\n")
File_append= File1.write(b)
File1.close()

File1=open('Output.txt','r')
print("Final content of Output.txt:")
file_read= File1.read()
print(file_read)
File1.close()
