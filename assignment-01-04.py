"""
4. Write a function that returns the largest number from an input list.
"""

def find_largest_number(numbers):
    largest_number = numbers[0]
    
    for i in range(1, len(numbers)):

        if numbers[i] > largest_number:

            largest_number = numbers[i]
        
    return largest_number

input_list = [23, 5, 9, 28]
b = find_largest_number(input_list)
print(b)
