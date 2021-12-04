# program to calculate the average of number 
a = int(input('Enter a first number: '))
b = int(input('Enter a second number: '))
c = int(input('Enter a third number: '))
d = int(input('Enter a fourth number: '))
e = int(input('Enter a fifth number: '))

average = (a + b + c + d + e) / 5
print(f'the average of five different number is: {average}')

# program to exchange the value of two different numbers with using temporary variable 
a = 10
b = 20

# swipping the value of variable here 
_ = a
a = b 
b = _
# printing the above swipped value here 
print(f'the value of a is: {a}')
print(f'the value of b is: {b}')


# program to exchange teh value of two numbers with out using temporary variables 
x = int(input('Enter a first number to swap: '))
y = int(input('Enter a second number to swap: '))

x = x + y 
# x = 10 + 20 = 30
y = x - y
# y = 30 - 20 = 10
x =  x - y
# x = 30 - 10 = 20
print(f'the value of first number is {x}')
print(f'the value of second number is {y}')


# program to read a number n and compute n+nn+nnn 
a =  int(input('Enter a number: '))
s = str(a)
sum1 =  s + s
# -----> 55
sum2 = s + s + s
# ---> 5 5 5
compute =  a + int(sum1) + int(sum2)
# ------> 5 + 55 + 555
print(f'the value after computing: {compute}')
# ------> 615


# program to read two number and print their quotation and remainder 
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

# remainder and quotent 
ans =  divmod(a, b)
print(f'the quotient and remaindr of {a} and {b} is {ans}')