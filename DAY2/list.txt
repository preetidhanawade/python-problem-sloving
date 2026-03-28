#Ex.1 WAP To Perform List Slicing
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
print(mylist)  
print(type(mylist))  
print(mylist[0])  
print(mylist[1])   
print(mylist[2])  
print(mylist[-1])  
print(mylist[2:5])  
print(mylist[:5])   
print(mylist[1:])  
print(mylist[1:8:2])

#----Output----
#['prashant', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant']
#<class 'list'>
#prashant
#Ashish
#komal
#prashant
#['komal', 'ankush', 'Ashish']
#['prashant', 'Ashish', 'komal', 'ankush', 'Ashish']
#['Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant']
#['Ashish', 'ankush', 77, 60.52]

#Ex.2 WAP to check list is mutable means change the value
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
mylist[0]="Akshay"  
print(mylist)

#----Output----
#['Akshay', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant']

#Ex.3) WAP to add the new object in list using ‘append()’ function at the end of list
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52]
mylist.append('harsh')  
mylist.append("laxman")  
print(mylist)

#----Output----
#['prashant', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant', 'harsh', 'laxman']

#Ex.4) WAP  to add an item at specified position using ‘ insert()’ function 
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52]
mylist.insert(1,"sanket")  
print(mylist)

#----Output----
#['prashant', 'sanket', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant']


#Ex.5) WAP to write Slicing string
name="prashantjha"
#indexing=012345678910
print(name[0])#p
print(name[1])#r
print(name[-1])#a
#print(name[15]) Error string index out of range
print(name[0:5])#end-1,5-1=4,prash
print(name[1:])#rashantjha
print(name[:5])#5-1=4 prash
print(name[:])#prashantjha
print(name[1:8:2])#'''8-1=7=rsat
print(name[::-1])#ahjtnahsarp

#----Output----
#p
#r
#a
#prash
#rashantjha
#prash
#prashantjha
#rsat
#ahjtnahsarp

#Ex.6) WAP to clone the list means copy all objects from one list and creating new list
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52]
newlist = mylist.copy()    # copy() will copy everything from mylist and returns
print(mylist)
print(newlist)

#----Output----
#['prashant', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52]
#['prashant', 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52]

#Ex.7) WAP for multidimensional list
mylist = [ [ 'virat',  'kohli' ], [ '85.56' ], [ 440022, "yyy" ] ]      
print("example of multidimensional list: ")      
print(mylist)      
#print(mylist[row][col])   first square bracket represent row and second represent col      
print(mylist[0][0])      
print(mylist[0][1])      
print(mylist[1][0])      
print(mylist[2][0])      
print(mylist[2][1])     

#----Output----
#example of multidimensional list: 
#[['virat', 'kohli'], ['85.56'], [440022, 'yyy']]
#virat
#kohli
#85.56
#440022
#yyy

#Ex.8) Use List functions del(), clear(), list(), reverse(), sort(), sort(reverse=True), id(), count(), pop()

# Deleting a particular index value using 'del' keyword
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]  
list2 = [50, 25.50, 'prashant']  
del list2[2]  
print(list2)  # Output: [50, 25.5]  
  
# Deleting the list from memory using 'del' keyword   
list2 = [50, 25.50, 'prashant']  
del list2  
# print(list2) would raise NameError  
  
# Clearing the elements of a list  
list2 = [50, 25.50, 'prashant']  
list2.clear()  
print(list2)  # Output: []  
  
# List typecasting using 'list()' function  
name = "prashant"  
print(name)  # Output: prashant  
myname = list(name)  
print(myname)  # Output: ['p', 'r', 'a', 's', 'h', 'a', 'n', 't']  
  
# Reversing a list using 'reverse()' function  
mylist = [40, 30, 20, 10]  
mylist.reverse()  
print(mylist)  # Output: [10, 20, 30, 40]  
  
# Sorting a list using 'sort()' function  
mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort()  
print(mylist)  # Output: [0, 9, 22, 44, 77, 88]  
  
# Sorting a list in descending order  
mylist.sort(reverse=True)  
print(mylist)  # Output: [88, 77, 44, 22, 9, 0]  
  
# Implementing aliasing concept  
mylist = [44, 22, 77, 0, 9, 88]  
newlist = mylist  
print(id(mylist))  # Output: same id  
print(id(newlist))  # Output: same id  
  
# Implementing 'count()' function  
n = [1, 2, 3, 5, 5, 5, 1, 2, 4, 4, 6, 6, 6]  
print(n.count(1))  # Output: 2  
print(n.count(2))  # Output: 2  
print(n.count(3))  # Output: 1  
print(n.count(4))  # Output: 2  
print(n.count(5))  # Output: 3  
print(n.count(6))  # Output: 3  
print(n.count(7))  # Output: 0  
  
# Returning the last element using 'pop()' function  
list1 = [3, 4, 5, 6, 7]  
print(list1.pop())  # Output: 7  




