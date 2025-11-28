list = ["ganesh", 123, 23.4, True]
print(list)
# now we will see some list methods
list.append("salunke")          # it will add item at the end of the list
print(list)

l1= [1,4,2,5,3]
#l1.sort()           # it will sort the list in ascending order
l1.reverse()         # it will reverse the list
print(l1)

l2= [1,2,3,4,5]
l2.insert(2,"hi")    # it will insert item at specified index
print(l2)

l3= [1,2,3,4,5]
print(l3.pop(3))             # it will remove item at specified index
print(l3)

l4= [1,2,3,4]
l4.remove(1)          # it will remove first occurance of specified item
print(l4)
