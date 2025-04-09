'''
1.Conditional: if-else, if-elif
2.Looping: for, while
3.jumpping: break, continue, pass
'''
def checkAge(age):
    if(age>18):
        print("Age is greater then 18")
    else:
        print("Age is not grater then 18")
checkAge(18)

# WAP to diplsy "Child" if age is below 18, display "Adult " is the above 18, 
# dislay senior Citizen if age is above 65.

def displayAgeCatagory(age):
    if(age<18):
        print("Child")
    elif(age>=18):
        print("Adult")
    elif(age>65):
        print("Senoier Citize")
displayAgeCatagory(int(input('Enter age')))