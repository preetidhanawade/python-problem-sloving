Ex.1) WAP to take input and display output of tuple and understand the above points:

mytuple = ("virat", "Ashish", "Rahul","sandip","komal","ankush","rajesh",23,3.15,77,"sandip")  
print(mytuple)  
print(type(mytuple)) 

#----Output----
#('virat', 'Ashish', 'Rahul', 'sandip', 'komal', 'ankush', 'rajesh', 23, 3.15, 77, 'sandip')
#<class 'tuple'>

Ex.2) WAP to check tuple is immutable or not:

mytuple = ("virat", "Ashish", "Rahul","sandip","komal","ankush","rajesh",23,3.15,77,"sandip")  
mytuple[2]="sunil"  
print(mytuple) 

#----Output----
#TypeError: 'tuple' object does not support item assignment

