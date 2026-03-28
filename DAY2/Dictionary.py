WAP for implementing dictionary and its function:

# Example 1: Take input as key-value pair and display output  
mydict = {  
  "name": "prashant",  
  "professional": "developer",  
  "empid": 1001   
}  
print("Example 1 Output:", mydict)  
print(type(mydict)) 

#----Output----: {'name': 'prashant', 'professional': 'developer', 'empid': 1001}
#<class 'dict'>


# Example 2: Take input as key and display the value  
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}  
a = mydict[102]  
print("Example 2 Output:", a)  
  
#----Output--- : ashish


# Example 3: Change values with the help of keys  
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}  
mydict[102] = "peter"  
print("Example 3 Output:", mydict)  

#----Output---- : {101: 'ashish', 102: 'peter', '103': 'mohini', '104': 'trivani', 104: 'ashish'}


# Example 4: Print only keys using a loop 
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}   
for x in mydict:  
     print("Output:", x)  

#----Output----
#101
#102
#103
#104
#104


# Example 5: Print only values using values() function
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}   
for x in mydict.values():  
     print("Output:", x)  
  
#---- Output----:  
# ashish  
# ashish  
# mohini  
# trivani  
# ashish  


# Example 5: Print only values using values() function
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}   
for x in mydict.values():  
     print("Output:", x)  
  
# ----Output----:  
# ashish  
# ashish  
# mohini  
# trivani  
# ashish  

# Example 7: Add a new key-value pair  
mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}   
mydict["mobile_no"] = 4646463738  
print("Output:", mydict)  

#----Output----
#{101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'trivani', 104: 'ashish', 'mobile_no': 4646463738}

# Example 8: Remove key-value pair using pop() function 
mydict = {  
  "name": "Vasundhara",  
  "professional": "developer",  
  "empid": 1001   
}  

mydict.pop("empid")
print("Output:", mydict)  

#----Output----
#{'name': 'Vasundhara', 'professional': 'developer'}


# Example 9: Create a clone of the dictionary
mydict = {  
  "name": "Vasundhara",  
  "professional": "developer",  
  "empid": 1001   
}    
newdict = mydict.copy()  
print("Example 9 Output:", newdict)  

#----Output----
#{'name': 'Vasundhara', 'professional': 'developer', 'empid': 1001}








