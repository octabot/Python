def count_on_fingers(n: int) -> int:
    remainder = n % 8
    
    if remainder == 1:
        return 1  # Thumb
    elif remainder == 2 or remainder == 0:
        return 2  # Index finger
    elif remainder == 3 or remainder == 7:
        return 3  # Middle finger
    elif remainder == 4 or remainder == 6:
        return 4  # Ring finger
    else:  # remainder == 5
        return 5  # Little finger

# Dry run with given interview example N = 14
print(count_on_fingers(9))  # Output: 4 (Ring finger)