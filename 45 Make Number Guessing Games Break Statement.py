student=[]

while True:
    name=input("Enter student name:")
    if name =='shesh':
        print(student)
        print("total student:",len(student) )
        break
    else:
        student.append(name)

