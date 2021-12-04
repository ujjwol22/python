import math
a = 2.3
print(math.ceil(a)) # passes the greater value than given number 
print(math.floor(a)) # passes the smallest value then given number


# in the case of boolean, if we compare the value with any other value (string int float etc ) it will be true 
a = 10
if a == 0 or 5:
# if a == 0 or 'Ujjwol':
    print('hello')
else:
    print('bye')

if a == 10 or 5:
    print('Ujjwol is true')
else:
    print('Ujjwol is false')



# is 
# is not  // it checks the  value in memory 
a = 5
b = 5
print(a is b) # returns either true ot false 
print(a is not b) # returns either true ot false 

# id() this checks the memory address of any var 
print(id(a))
print(id(b)) # returns a same memory address 

a = 'Ujjwol'
b = 'Ujjwol'
print(id(a))
print(id(b))
print(a is b)

# in case of list set and tuple the memory address will be diffferent although they have same value  as shown below 
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)

a = [1, 2]
b = a
print(id(a))

# set 
a = {1, 2, 3}
b = {1, 2, 3}
print(id(a))
print(id(b))
print(a is b)

# tuple; why this is showing true value ?
p = (1, 2, 3)
q = (1, 2, 3)
print(id(p))
print(id(q))
print(p is q) 


# use of in in python  
a = [1, 2, 3]
print(1 in a)
print('1' in a)

b = [1, 2, '1', '2']
print('1' in b)
print(2 in b)

a = 'Ujjwol'
print('y' in a)
print(a[0] in a)

x = 20
y = 18
list = [21, 18, 40, 24, 30]
if x not in list: # statement is saying true 
    print('x is not in list')
else:
    print('x is in list')

if y in list:
    print('y in list')
else:
    print('y is not in list')


# between AND & OR, AND have high presidence 
# AND have high presidence 
name = 'Ujjwol'
age = 0
if name == 'Ujjwol' or name == 'mahesh' and age >= 2:
    #              ----> this will execute at first becasue and operator have high presidence 
    print('The condition is true')
else:
    print('The condition is false')