'''
String are Immutable:
1.once we declare the string we cannot modify it. if we try to modify the string it will create new string
2.if new does noit have a refrence variable then it will be removed
3. python Internally uses String Interning
4.String interning is the process of checking string intern pool creating any new object
5 whenever we want to create new object, python first will check String intern pool weather that object already exits or not
6.when object alredy exits in the string intern records  then address of existing object will be reused
'''

#s1 = 'kodnest'
#s2 = s1.upper()
#print(s1)
#print(s2)

#s1 ='k'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))

print("S1 Id of H:",id(s1[0]))
print("S2 Id of W:",id(s1[0]))

print("S1 Id of O:",id(s2[-1]))
print("S2 Id of O:",id(s2[1]))

print("S1 Id of l:",id(s1[2]))
print("S1 Id of l:",id(s1[3]))
print("S2 Id of l:",id(s1[3]))
