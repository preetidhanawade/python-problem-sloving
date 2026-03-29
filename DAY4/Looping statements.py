#--------------For Loop--------------
#Ex1)s = "Ashish Gadpayle"  
for x in s:  
    print(x) 
#-----output-----
#A
#s
#h
#i
#s
#h

#G
#a
#d
#p
#a
#y
#l
#e


# Eg 2: To print characters present in string index-wise  
s = input("Enter some String: ")  
i = 0  
for x in s:  
    print("The character present at", i, "index is:", x)  
    i += 1  
#----------------- Output (Example input: 'Python'):----------  
# The character present at 0 index is: P  
# The character present at 1 index is: y  
# The character present at 2 index is: t  
# The character present at 3 index is: h  
# The character present at 4 index is: o  
# The character present at 5 index is: n  



# Eg 3: To print Hello 5 times  
for x in range(5):  
    print("Hello")  
# ----------Output:  -------------
 #Hello  
 #Hello  
 #Hello  
 #Hello  
 #Hello  

# Eg 4: To display numbers from 0 to 10  
for x in range(11):  
    print(x)  
#--------- Output:------  
# 0 1 2 3 4 5 6 7 8 9 10 


# Eg 5: To display odd numbers from 0 to 20  
for x in range(21):  
    if x % 2 != 0:  
        print(x)  
#---- Output:----------- 
# 1 3 5 7 9 11 13 15 17 19  


# Eg 6: To display numbers from 10 to 1 in descending order  
for x in range(10, 0, -1):  
    print(x)  
# -----------Output: ------ 
# 10 9 8 7 6 5 4 3 2 1  
  
  
# Eg 7: To print sum of numbers present inside list  
lst = eval(input("Enter List: "))  
sum = 0  
for x in lst:  
    sum += x  
print("The Sum=", sum)  
# -----Output :-----
#Example input: [1,2,3,4,5]):  
# The Sum= 15  


While Loop:

If we want don't know about range, then we should go for while loop.

Syntax:

    

---------------WHILE LOOP-----------------------------
Ex.5) WAP to print hello world five times using While loop:

count = 0  
while count < 5:  
    print("Count:", count)  
    count += 1  
Output:

Hello World 0

Hello World 1
Hello World 2
Hello World 3
Hello World 4


#------------BREAK LOOP--------------------
#EX1)Break() function 
for i in range(1,5): #i=3
    if i==3:
        break
    print(i)
--------------OUTPUT-----------
#1
#2
--------------CONTINUE LOOP-------------
#EX1).
for i in range(1,5): #i=3
    if i==3:
        continue
    print(i)
#---------OUTPUT--------
#1
#2
#4

#EXP2)
mycart=[10,20,200,300,800,60,700]
for i in mycart:     #i=1:20
    if i>400:
        print("This my purchased cart item")
        continue
    print(i)
#-----------OUTPUT----------
#10
#20
#200
#300
#This my purchased cart item
#60
#This my purchased cart item
