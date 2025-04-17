'''
In tuple we can store Homogeneous as well as Heterogeneous data.
In tupels we can store duplicatio
Tuples are ordered collection of data
Tuples are Immutable: once we declare the tuple we cannot modify it.
'''
tup1 = (10, 22.55, 'Kodnest',True,10)
print(tup1)
# tup1.remove(55)
# tup1.pop()
# del tuple[2]
print(tup1[2])

#Deletes the complete tup1 object
del tup1
#print(tup1) #Error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)

# create a Single Tuple
tup = (10,)
print(tup, type(tup))

new_tup = (10,20,30,40)
# ele1 = new_tup[0]
# ele2 = new_tup[1]

#Unpackin of tuple
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1',ele1)
