# Homework 3 - Functions + Conditionals + Loops
# Mackenzie Tam


def say_goodbye(name):
    print("goodbye,", name)


def circle_area(radius):
    area = 3.14 * radius**2
    print("the area of the circle is", area)


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def temperature_range(temperatures):
    minimum = min(temperatures)
    maximum = max(temperatures)
    return (minimum, maximum)


def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False


def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used


def secret_code(number):
    last_digit = number % 10
    remaining_number = number // 10
    digits = len(str(remaining_number))
    encrypted_number = last_digit * (10**digits) + remaining_number
    return encrypted_number


def power(x, y):
    result = 1

    for i in range(y):
        result = result * x

    return result


def minimum_for(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


def maximum_for(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def minimum_while(numbers):
    minimum = numbers[0]
    index = 0

    while index < len(numbers):
        if numbers[index] < minimum:
            minimum = numbers[index]

        index += 1

    return minimum


def maximum_while(numbers):
    maximum = numbers[0]
    index = 0

    while index < len(numbers):
        if numbers[index] > maximum:
            maximum = numbers[index]

        index += 1

    return maximum


def sum_digits(number):
    total = 0

    while number > 0:
        last_digit = number % 10
        total = total + last_digit
        number = number // 10

    return total


x = 2
y = 3
result = power(x, y)

print(f"the result of Oski stole your power with x = {x} and y = {y} is {result}.")