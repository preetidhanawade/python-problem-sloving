Day 5;
1.#find max and min value in the given array=[5,3,9,2,6]
arr=[5,3,9,2,6]
max_val=arr[0]
min_val=arr[0]
for i in arr:
    if  i> max_val:
        max_val=i
    if  i< min_val:
        min_val=i
print("max_val",max_val)
print("min_val",min_val)

2.#Find the second largest element in the given arr
list=[7,3,9,2,8]
list.sort()
print(list)
print(list[-2])

3.#expexted by output is[1,3,12,0,0]
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

3.# Find Common elements in an given array
A=[1,2,3]
B=[2,3,4]
C=[3,4,5]

for i in A:
    if i in B and i in C:   #using AND operation
        print(i)
Ans:3

while loop syntax:
initialization
while condition:
   #statement
   #increment

4.#While loop 
i=1  #i=1
while i<5:
    print(i)
    i=i+1
    
5.#find total even and odd numbers
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

6.#WAP for this while loop
1+2+3+4+5+6+7+8+9+10=55
Ans:
sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print(sum)

7.
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

Ans:
