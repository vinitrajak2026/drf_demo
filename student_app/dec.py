def find_odd(func):






"""this function will return a count the sum of occurence of no of a given list"""
def find_numbers_decorator(func):
    def wrapper(numbers, target):
        result = func(numbers, target)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found")
        return result
    return wrapper

@find_numbers_decorator
def find_no(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

numbers_list = [1, 2, 3, 4, 5]
target_element = 4

find_no(numbers_list, target_element)



