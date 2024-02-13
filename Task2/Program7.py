#Factorial using for

num = int(input("enter the number"))
fact = 1
if num == 0:
    print("factorial of ", num,"is 1 ")
elif num < 0:
    print("invalid input")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)


#Factorial using while

num = int(input("Enter the number"))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
    print(fact)


#Fibonacci series

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b




