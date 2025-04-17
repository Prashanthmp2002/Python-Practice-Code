l1 = [1,2,3,4,5]
# print(l1) #[1, 2, 3, 4, 5]
# sq_li = [] #[1, 4, 9, 16, 25]
# for i in l1:
#     sq_li.append(i**2)
# print(sq_li)


duplicate_li1 = [i for i in l1]

# when we have only if part then write it after for loop 
even = [i for i in l1 if i%2 ==0]
sq_list = [i**2 for i in l1]
new_li1 = [ele+2 for ele in l1]

#when we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in l1]

#Multipule for loops inside list comprehesion
li = [[10,20],[30,40],[50,60]]
new_li =[ele for sublist in li for ele in sublist]