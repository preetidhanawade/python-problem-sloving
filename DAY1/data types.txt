# Ex1. WAP to check the Datatype of Variable
name = 'poorva'  
marks  = 80  
percentage = 93.5  
complex_value = 2+8j  
passed    = True  
print('Display the output:')  
print('Name (Data type=):', type(name))  
print('Marks(Data type=):', type(marks))  
print('Percentage(Data type=):', type(percentage))  
print('Complex value(Data type):', type(complex_value))
print('Passed status(Data type=):', type(passed))

#output(
#Display the output:
#Name (Data type=): <class 'str'>
#Marks(Data type=): <class 'int'>
#Percentage(Data type=): <class 'float'>
#Complex value(Data type): <class 'complex'>
#Passed status(Data type=): <class 'bool'>)

# Ex2. WAP how to check the address of the variables
name = 'Poorva'  
print('Name(Address=) :',id(name))  

# Output:
#Name(Address=) : 2282952805328

#Ex3.WAP to check if three variables have the same value so all the three variable addresses are the same. ( Using id() function we can check the address)
name = 'poorva'  
marks  = 80  
percentage = 93.5  
print(id(name))
print(id(marks))
print(id(percentage))

#output
#2337282280400
#140720434011736
#2337282022576


