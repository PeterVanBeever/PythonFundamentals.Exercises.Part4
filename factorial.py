def recur_factorial(n):
    if (n ==1 or n ==0):
        return 1
    else:
        return (n * recur_factorial(n-1))
    
num = 7
print(num)

print("Factorial is" , recur_factorial(num))
