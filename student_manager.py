student ={}
while True:
    print("\n----STUDENT MANAGER APP----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Student result")
    print("4. Exit")
    
    choice=input("enter your choice=")
    #  adding student..
    if choice=="1":
        name=input("enter student name= ")
        marks=int(input("enter student marks= "))
        student[name]=marks
        print(f"{name} is successfully added!!")
    # view students..
    elif choice=="2":
        if not student:
            print("No student found!!")
        else:
            for name,marks in student.items():
                print(name, ":", marks)
    # checking result...
    elif choice=="3":
        name=input("enter Student name= ")
        if name in student:
            marks=student[name]
            
            if marks>=40:
                print(f" STUDENT {name} PASS SUCCESSFULLY!!")
            else:
                print(f" student {name} FAIL!")
        
        else:
            print("student not found!!")
            
            
    # exit
    elif choice=="4":
        
        print("EXITING....")
        break
    else:
        print("invalid input!!!")