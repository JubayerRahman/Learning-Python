def find_max_value(numbers):
    max_value = numbers[0]

    for number in numbers:

        if number> max_value:
            max_value = number

    return max_value

numbers = [12, 45, 3, 99, 7, 88, 1000]
print(find_max_value(numbers)) 