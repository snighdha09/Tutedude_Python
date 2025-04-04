d={'Alice':85,'Bob':67,'David':98}
a=input("Enter the student's name: ")
if (a in d)==True:
    print(a,"'s Marks:",d.get(a))
else:
    print("Student not found.")
