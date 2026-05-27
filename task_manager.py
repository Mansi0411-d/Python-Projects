def task():
    tasks=[]
    print("---------welcome to Task Manager APP-------")
    total_task=int(input("enter how many tasks u want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"enter task {i}= ")
        tasks.append(task_name)
        
    print(f"today's tasks are\n {tasks}")
    while True:
        operation=int(input(" Enter 1- Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit/Stop"))
        if operation==1:
            add=input("enter task u want to add=")
            tasks.append(add)
            print(f'Task {add} has been successfully added...!!')
            
        elif operation==2:
            updated_val=input("enter task u want to update= ")
            if updated_val in tasks:
                up=input("enter new task now= ")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task is {up}")
        elif operation==3:
            del_val=input("which value u want to delete= ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f" task {del_val} has been deleted..!!")
        elif operation==4:
            print(f"total tasks={tasks}")
        elif operation==5:
            print("closinng the prog...!!")
            break
        else:
            print("invalid choice!!!!")

task()