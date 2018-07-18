# List all tasks
# Add a task to the list
#Delete a task
#  Quit the program

#taskText = ("Congratulations! You're running [YOUR NAME]'s Task List program.What would you like to do next?
 #           1. List all tasks.
  #          2. Add a task to the list.
   #         3. Delete a task.
    #        4.To quit the program""

opener = "Congratulations! Your're running" + input("entername")+ "'s Task List program!"
opener2=  "What would you like to do next?"
step1 = "1.List all tasks"
step2= "2.Add a task to the list"
step3 = "3.Delete the task"
step4 = "4.To quit the program"
myList = ["Sonic", "is", "Awesome "]
whatsNext= input( "Whats next?"+"List ,Add ,or Delete?")  # if what                    # My list of actions # substitute tasks for index really
# if 0 == = run the code, and use q to quit when I want !
newTask = input()

def taskProgram():
    print(opener)
    print (opener2)
    print (step1)
    print (step2)
    print (step3)
    while 0 >=0:
        #print (whatsNext)
        if whatsNext == "List":
                print (myList)
                break
        if whatsNext == ("Add"):
            myList.append(newTask)
            print (myList)
            break
        if whatsNext ==("Delete"):
            myList.remove(myList[0])
            print (myList)
            break




 #   for index in myList:
#        print (myList

 #if user task = list run a code that makes a lis tof my array
 #if user task = add , run a code that adds a task ( index to the list)
 #if user task = delete  run a code that deletes a task( index)
 # use q to  quit the program at any time
# use continue to keep loop gooing
#use a while  loop since this is repeating
#print (myList)

   # print (opener,opener2)


print (taskProgram())