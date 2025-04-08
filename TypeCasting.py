#if String is holding interger then it can be converted into int.
a = '30'
print(a,type(a))
b = int(a)
print(b,type(a))

# str to interger conversion is not allowed
x = 'kod'
print(x,type(x))
#y = int(x)
#print(y,type(y))

p = float(input("Enter float type date")) # 12.22
print(p,type(p))

#bool()
q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))

q = 0
print(q, type(q))
q = bool(q)
print(q, type(q))

q = " "
print(q, type(q))
q = bool(q)
print(q, type(q))


'''
1.While converting int to bool for all non ero values we will get true
2.while converting int to bool for 0 and empty string we will get flase
'''