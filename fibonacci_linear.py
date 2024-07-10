def find_fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    
    # initialize first 2 in sequence
    # special case for 0 and 1
    current = 0
    next  = 1

    # begin loop at 2, not 0 or 1
    for i in range(2, position +1):
        added_num = current + next
        # set current to next
        current = next
        # set next to added_num
        next = added_num

    return next

position = 9
n = position

print(position, find_fibonacci(position))
