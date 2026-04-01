Day 5:
---------------------------------------------------------------
#Find the second largest element in the given arr
list=[7,3,9,2,8]
list.sort()
print(list)
print(list[-2])
-----OUTOUT------
#max_val 9
#min_val 2


#expexted by output is[1,3,12,0,0]
list=[0,1,0,3,12]
list.sort(reverse=True)
print(list)

or

list=[0,1,0,3,12]
for i in list:  #i=2
    if i==0:
        list.remove(i)
        list.append(i)
print(list)
----------OUTPUT-----------
#[12, 3, 1, 0, 0]

# Find Common elements in an given array
A=[1,2,3]
B=[2,3,4]
C=[3,4,5]

for i in A:
    if i in B and i in C:   #using AND operation
        print(i)
Ans:3
-------------OUTPUT-----------
while loop syntax:
initialization
while condition:
   #statement
   #increment



#While loop 
i=1  #i=1
while i<5:
    print(i)
    i=i+1
  -----OUTPUT-------------
#1
#2
#3
#4

#find total even and odd numbers
even=0
odd=0
i=1 #i
while i<=10:
    if i%2==0:
        even=even+1
       
    else:
        odd=odd+1
    i=i+1
print("Even=",even)
print("Odd=",odd)
------OUTPUT-----------
#Even= 5
#Odd= 5


#
for i,j in zip(range(1,6),range(5,0,-1)):  #i=3,j=3

    if i==3 and j==3:  #here if the value if i and j is equal then take continue 
        continue
    print(i," ",j)
Ans:5,4,2,1

8.#Nested for loop
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()
