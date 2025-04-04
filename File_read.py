try:
    File1= open('Sample.txt','r')
    read_file=File1.read()
    print(read_file)
    File1.close()
except FileNotFoundError:
    print("Error:The File 'Sample.txt' was not found")

