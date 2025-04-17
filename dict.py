# dict is mutable
d1 = {
    'name': 'Prashi',
    'Age': 24,
    'Phone' : 34567
}
print(d1,type(d1)) #{'name': 'Prashi', 'Age': 24, 'Phone': 34567} <class 'dict'>

d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'Age': 24, 'Phone': 34567}

d1['Age'] = 29
print(d1) #{'name': 'Pooja', 'Age': 29, 'Phone': 34567}

# In dict we can store duplicate values.
marks = {'sci':'85','Math':'85'} #Allowed
print(marks)

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)

    list(),tuple(),set(),dict()
