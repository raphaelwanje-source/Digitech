# creating a list
my_list=[1,2,3,4]
print(my_list)

# Append method: adds an item  x to the end of existing list
my_list.append(5)
print(my_list)

# extend method appends all items from am iterable to the end of the list

my_list.extend([6,7,8])
print(my_list)

# Insert(i,x): inserts an item x at a specific position i in the list
my_list.insert(2,9)
print(my_list)

# remove (x): removes the first occurences of item x in the list
my_list.remove(9)
print(my_list)

# pop[i]: removes and returns the item at index i (default is the last item)
popping=my_list.pop(7)
print(my_list, "removed element is :", popping)

# index(x): returns the index of the first occurence of item x in the list 

# count (x): retruns the number of occcurences of item x in the list 
counting=my_list.count(4)
print(counting)

# sort()sorts the list in ascending order
my_list.sort()
print(my_list)

# reverse(): reverses the order of items in the list
my_list.reverse()
print(my_list)

length=len(my_list)
print(length) 

maximum=min(my_list)
print(maximum)

checking =3 in my_list
print(checking)

checking =3 not in my_list
print(checking)

Raphael=my_list.copy()


my_list.clear()
print(my_list)

# I want to retrieve cleared data
print(Raphael)
