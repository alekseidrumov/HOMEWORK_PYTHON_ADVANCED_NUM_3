def search_max(numbers):
    max = 0 
    for num in numbers:
        if num > max:
            max = num
    return max 

print(search_max([11, 99, 3, 100]))


