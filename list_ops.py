#List Operations

provincies = ['Groningen','Drente', 'Limburg', 'Friesland', 'Gelderland' ]

#give the command for the length of the element Drente
print(provincies[0])

#Add an element to the list
provincies.insert(0,'Zuid-Holland')
print(provincies)

#Make a list selection with the last 6 elements of a list of unknown length
list_unknown = []
list_selectie = list_unknown[:-6]

#Count how many items are there in the list
print(provincies.count('Drente'))

#Append 'Texel'to the list
provincies.append('Texel')
print(provincies)

#Index, returns the position of a given element
print(provincies.index('Zuid-Holland'))

#Remove, removes element from the list
provincies.remove('Zuid-Holland')
print(provincies)

#Reverse, reverses the elements in the list. List is modified
# provincies.reverse()
# print(provincies)

#Sort(s) elements of the list in asc. order.List is modified
# provincies.sort()
# print(provincies)

provincies.insert(0,'Amsterdam')
provincies.insert(0,'Zeeland')
provincies.insert(0,'Gorinchem')
print(provincies)

#Sorted, returns a sorted list. List not modified.
print(sorted(provincies))

#Zip 2 list together
a = ['x', 'b', 'z', 'a']
b = ['hello', 'hola', 'adiós', 'au revoir']

new_list = list(zip(a,b))
print(new_list)
alpha = sorted(list(zip(a,b)))
print(alpha)

#List comprehension
a_list = [i**3 for i in (1,2,3,4,5,6,7)]
print(a_list)

#Difference between 2 lists

list1 = ['Scott', 'Kelly', 'Eric', 'Thomas']
list2 = ['Kelly','Thomas']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)

#Remove duplicate from list
q = [20,22,23,23,24,25,26,25,22,29,23,34,35]

new_list = list(set(q))
print(sorted(new_list))
