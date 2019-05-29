import sys
import todo_list, todo_add, todo_check, todo_remove

if sys.argv[1] == "-l":
    rows = todo_list.todolist()
    for i in rows:
        print(i)

elif sys.argv[1] == "-a":
    rows = todo_add.todoadd(sys.argv[2])  
    for i in rows:
        print(i)  

elif sys.argv[1] == "-c":
    rows = todo_check.todocheck(sys.argv[2])
    for i in rows:
        print(i)

elif sys.argv[1] == "-r":
    rows = todo_remove.todoremove(sys.argv[2])
    for i in rows:
        print(i)