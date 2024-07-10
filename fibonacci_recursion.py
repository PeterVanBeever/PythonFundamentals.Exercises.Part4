def fibonacci(n):
    
    if n <0 or n>30: # can't be negative start
        pass
    elif n == 0: # has to start at 0
        return 0
    elif n == 1 or n == 2: # position 1 = 1, position 2 = 1
        return 1 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
            # returns addition of last two numbers for next number
print(fibonacci(30))