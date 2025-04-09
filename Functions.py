#without input and without return statement
def add():
    a = 10
    b = 20
    print('Addtion is:',a+b)


#with input and without retun statement
def sub(a, b):
    print('Subtraction is:',a-b)

#without input and with return statement:
def mul():
    return 10*20

#with input with return statement
def div(a,b):
    return a/b


add()
sub(100,50)
print(mul())
print(div(200,10))