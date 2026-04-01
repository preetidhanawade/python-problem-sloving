Day-6:
1.#predefine module
import math
print(math.sqrt(16))
print(math.pi)

2.
from math import*
print(int(sqrt(4)))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))

3.#random module:
#This module defines several functions to generate 
#random numbers
#We can use these functions while developing games
from random import*
for i in range(5):  #0-4
    print(random())

4.#To generate a random integer between two given
  #numbers(inclusive)
from random import*
for i in range(5):  #0-4
    print(randint(1,100000))

5.#Choice() function:
  #It wont return number
  #It will return a random object from the given list or tuple

from random import*
list=["prashnta","rahul","ashish","sandip","sunil","nikhil"]
for i in range(10):
    print(choice(list))

6.(i)module1
def welcome(fname,lname):
    print("Hello",fname)
    print("Hello",lname)
def login(username,password):
    if username==password:
        print("You have login successfully")
    else:
        print("You have entered wrong username and password")
def square(num):
    print("square of two no=",num*num)
pi=3.141592653589793

6.(ii)module2
import module1 as mod
mod.login('user','user')
print(mod.pi)
mod.square(4)

     or
6.(iii)module2
from module1 import pi,square,login,welcome
print(pi)
square(4)
login('user','user')
welcome('prashant','jha')
     
    or
6.(iv)module2
from module1 import*
square(4)
login('prashant','prashant')
print(pi)
welcome('abc','abc')

7.
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
Ans:Error come

8.
a=[1,2,3,4,5]
print(a[3:0:-1])
Ans:[4,3,2]

9.
def fun(value,values):
    var=1
    values[0]=44
t=3
v=[1,2,3]  #[44,2,3]
fun(t,v)
print(t,v[0])
Ans:3,44

10.
arr=[[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop())
Ans:4,7,11,15

11.
def f(i,values=[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3)

11.
fruit_list1=['Apple','Berry','Cherry','Papaya']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]
fruit_list2[0]='Guava'
fruit_list3[1]='Kiwi'

sum=0
for i in(fruit_list1,fruit_list2,fruit_list3):
    if list[0]=='Guava':
        sum+=1
    if list[1]=='Kiwi':
        sum+=20
print(sum)

12.
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i],end=" ")
Ans:2,3,4,5,6,6
