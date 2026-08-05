age = int(input("please enter your age:"))
if (age<18):
    print("You are not an adult.")
    if(age>=13):
        print("you are a teenager.")
elif(age<65):
    print("you are an adult.")
else:
    print("You are a senior citizen")


marks = int(input("please enter your marks:"))
if (marks>=70):
    print("A")
elif(marks>=55):
    print("B")
elif(marks>=40):
    print("C")
else:
    print("F")
