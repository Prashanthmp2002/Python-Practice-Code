#scripting way for writing the code
print("Hello world")

#Procedural way to writing the code
def message():
    print('Inside the method message:Hello world')
message()

#object Oriented way of writing code:
class Demo:
    def instance_method(self):
        print('Insude Instance method, Hello world')
d1 = Demo()
d1.instance_method()