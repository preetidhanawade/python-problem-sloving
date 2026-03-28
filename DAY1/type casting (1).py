# Ex1.int() used to convert in integer
print(int(3.14))
#print(int(10+5j))
print(int(True))#=1
print(int(False))#=0
#print(int("4.22"))
print(int("4"))
print(str("poorva"))

#output
#3
#1
#0
#4
#poorva


# Ex2. float() used to convert
print(float(3))#3.0
#print(float(50+2j))
print(float(True))#=1.0
print(float(False))#=0.0
print(float(4.22))
print(float("4"))

#output
#3.0
#1.0
#0.0
#4.22
#4.0


# Ex3.bool() is used to convert
print(bool(0)) 
print(bool(15))
print(bool(3.14))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool(" "))

#output
#False
#True
#True
#True
#False
#True
#False
#True
#True

# Ex4. complex() used to convert in complex
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
# print(complex("name"))
print(complex(5,-3))
print(complex(True,False))

#output
#(3+0j)
#(12.5+0j)
#(1+0j)
#0j
#(5+0j)
#(5.6+0j)
#(5-3j)
#(1+0j)

# Ex5.WAP to check if three variables have the same value so all the three variable addresses are the same. ( Using id() function we can check the address)
math = 50  
chemistry = 50  
physics = 50  
print('Address of Math =:', id(math))  
print('Address of Chemistry =:', id(chemistry))  
print('Address of Physics =:', id(physics))

#output
#Address of Math =: 140720428047000
#Address of Chemistry =: 140720428047000
#Address of Physics =: 140720428047000

# Ex6.WAP to check if values are different so memory addresses are different.
math = 50  
chemistry = 100
physics = 150 
print('Address of Math =:', id(math))  
print('Address of Chemistry =:', id(chemistry))  
print('Address of Physics =:', id(physics))

#output
#Address of Math =: 140720428047000
#Address of Chemistry =: 140720428048600
#Address of Physics =: 140720428050200





