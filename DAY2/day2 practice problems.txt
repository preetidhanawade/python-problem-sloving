# Ex.1)WAP to accept
n=int(input("Enter any single digit:"))
if n>0:
    print("positive number")
if n<0:
    print("negetive number")
if n==0:
    print("zero")

#----Output1----
#Enter any single digit:-9
#negetive number
#----Output2----
#Enter any single digit:5
#positive number

        
# Ex.2) WAP to accept 5 numbers in 5 different variables and check max number and input
n1=int(input("Enter the value of n1:"))#6
n2=int(input("Enter the value of n2:"))#5
n3=int(input("Enter the value of n3:"))#4
n4=int(input("Enter the value of n4:"))#2
n5=int(input("Enter the value of n5:"))#1
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print("N1 is max value")
if n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print("N2 is max value")
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print("N3 is max value")
if n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print("N4 is max value")
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
    print("N5 is max value")


#----Output----
#Enter the value of n1:5
#Enter the value of n2:8
#Enter the value of n3:6
#Enter the value of n4:2
#Enter the value of n5:5
#N2 is max value



# Ex.3) WAP to accept the three paper marks and calculate total,percentage and 
#if percentage is greater than or equal to 60 so he/she is eligible for placement drive

math=int(input("Enter marks of Maths:"))#70
chem=int(input("Enter marks of chem:"))#80
phy=int(input("Enter marks of phy:"))#90
total=phy+chem+math
percentage=total/3.0
print("Total =",total)
if percentage>=60:
    print("You are eligible for placement drive")
else:
    print("You are not eligible for placement drive")

#----Output----
#Enter marks of Maths:10
#Enter marks of chem:15
#Enter marks of phy:20
#Total = 45
#You are not eligible for placement drive


#Ex.4) WAP to calculate simple interest
pa=int(input("Enter principal amount:"))#100000
roi=int(input("Enter rate of interest:"))#1000
time=int(input("Enter the loan  amount duration:"))#100
si=pa*roi*time/100
print("Simple interest=",si)

#----Output----
#Enter principal amount:100000
#Enter rate of interest:1000
#Enter the loan  amount duration:100
#Simple interest= 100000000.0


# Ex.5) WAP to enter height of user in feet and convert it into inch and centemeter
height=float(input("Enter the height of user in feet:"))#5.5
inch=height*12#we get the value of inch
cm=inch*2.54
print("inch=",inch)
print("centemeter=",cm)

#----Output----
#Enter the height of user in feet:54
#inch= 648.0
#centemeter= 1645.92


# Ex.6) WAP to take centigrade temperature and convert it into fahrenheit temperature 
centi=float(input("Enter the centigrade temperature:"))#26.5
f=1.8*centi+240
print("Fahrenheit=",f)

#----Output----
#Enter the centigrade temperature:100
#Fahrenheit= 420.0


# Ex.7) Join function
s="preeti","suhasini","vasudhara"
m='|'.join(s)
print(m)

#----Output----
#preeti|suhasini|vasudhara


# Ex.8)Example of cases
s="Python is High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#----Output----
#python is high level programming language
#PYTHON IS HIGH LEVEL PROGRAMMING LANGUAGE
#pYTHON IS hIGH LEVEL PROGRAMMING lANGUAGE
3Python Is High Level Programming Language
#Python is high level programming language


# Ex.9) BODMAS
a=50
b=30
c=20
d=10
print((a+b)*c/d)#160
print((a-b)*(c/d))#40
print(a+(b*c)/d)#110

#----Output----
#160.0
#40.0
#110.0

