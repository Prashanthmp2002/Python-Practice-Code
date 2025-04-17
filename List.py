'''
1.List we can store Homogeneous as well as Heterogeneous Data.
2.In the list we can store duplicate values
3.List is an orderd collection of data: order of insetion will remain as it is in the output.
4.Lists are the mutable : once we declare the list we can modify it.
'''
li1 = [20, 30, 40, True, 'Kodnest',20]
print(li1, type(li1))


#append(): will add element at the end of the list
li1.append(300)
print(li1)

#insert(index, element): inserts an ele. at specified index.
li1.insert(1,15)
print(li1)

#remove(ele): remove the first occurrence of the specified ele.
li1.remove(20)
print(li1)


#in and not in operator:
print(2000 in li1)
print("Kodnest" in li1)

#pop(): Without argument will delete and return last ele. from list
removed_ele = li1.pop()
print(removed_ele)
print(li1)

#pop(index): with argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele)
print(li1)

del li1(1)
print(li1)