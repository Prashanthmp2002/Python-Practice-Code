
'''
1. In set we can store Homogeneous as well as Heterogeneous data.
2.Set is an unorderd collection of data.
3.set does not support indexing of data.
4.In set we cannot store duplicate
5. sets are mutable.
'''
s1 = {10, True, "kodnest", 10, 20, 55.44}
print(s1, type(s1)) #{True, 20, 55.44, 10, 'kodnest'} <class 'set'>
#print(s[10]) #Error

#add(): Used to add an element in the set
s1.add(500)
print(s1) #{True, 20, 500, 'kodnest', 55.44, 10}

s1.remove(55.44)
print(s1) #{True, 20, 500, 'kodnest', 10}

s1.pop()
print(s1) #{True, 20, 500, 10}

#pop() : Without index will delete and return one ele.333
poped_ele = s1.pop()
print(poped_ele) #20
print(s1) #{'kodnest', 500, 10}

#del s1[2] # Error
del s1

