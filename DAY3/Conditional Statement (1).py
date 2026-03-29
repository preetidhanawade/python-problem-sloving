#Ex.1) WAP to check no is negative or positive using Simple If Condition:
value = int(input('Enter any one number:'))  
if value>0:  
    print('Number is positive')  
if value<0:  
    print('Number is Negative')  
if value ==0:  
    print('Number is Zero')  
#------Output----------
#Enter any one number:2
#Number is positive
#Enter any one number:-2
##Number is Negative
#Enter any one number:0
#Number is Zero

#Ex.2) WAP to check a person is eligible for voter Id using if else condition:
age = int(input('Enter your ager to check voter id eligibility:'))  
if age>= 18:  
    print('You are eligible for voter Id')  
else:  
    print('You are not eligible')  
#-----------Output-------------
#Enter your ager to check voter id eligibility:20
#You are eligible for voter Id

#Ex.3) WAP to check biggest number among three numbers using else if ladder:
n1=int(input("Enter First Number:"))   
n2=int(input("Enter Second Number:"))   
n3=int(input("Enter Third Number:"))   
if n1>n2 and n1>n3:  
    print("Biggest Number is:",n1)  
elif n2>n3:  
    print("Biggest Number is:",n2)  
else :  
    print("Biggest Number is:",n3)  
#------Output---------
#Enter First Number:5
#Enter Second Number:2
#Enter Third Number:7
#Biggest Number is: 7

#Ex.4) WAP to check biggest number among three numbers using Nested if else:
a = int(input("Enter value of A:"))  
b = int(input("Enter value of B:"))  
c = int(input("Enter value of C:"))  
if a>b:  
     if a>c:  
           print("A is greater")  
     else:  
           print("C is greater")  
else:  
     if b>c:  
           print("B is greater")  
     else:  
             print("C is greater")  
#----Output-------
#Enter value of A:3
#Enter value of B:5
#Enter value of C:2
#B is greater

