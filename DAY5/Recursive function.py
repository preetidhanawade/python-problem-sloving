Ex.)  factorial(n)= n*factorial(n-1)


factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1

-------OUTPUT------------
=120



#Ex. WAP for recursive functions?

def factorial(n):  
      if n == 0:  
          return 1  
      return n * factorial(n - 1)  
print(factorial(5))   
Output:

#Output: 120


#Ex. WAP for subtraction of numbers using lambda function?


sub = lambda x,y: x-y
print("The result is :",sub(30-10))  
 
#Output:
#The result is : 20



#Ex: WAP to take another function as an argument?

num = [10, 20, 30, 40]
squared_number = list(map(lambda x: x**2, num))
print(squared_number) 
#Output:
#[100, 400, 900, 1600]



#Ex. WAP to use the filter() function?
list_val=[0,1,2,3,4,5,6,7,8,9]  
finalResult=list(filter(lambda x:x%2==0,list_val))  
print(finalResult)  
#Output:
#[0, 2, 4, 6, 8]
