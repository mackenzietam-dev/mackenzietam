
# Section 3.1

foods = ["juice", "banana", "orange", "mango", "kiwi"]

print(foods[1])
print(foods[-1])

foods.append("strawberry")
foods.insert(0, "apple")
print(foods)

del foods[2]
print(foods)

print(len(foods))

for food in foods:
    print(food.upper())

new_list = foods[0:1] + foods[-1:]
print(new_list)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# Error 1: I got a NameError because I wrote potato without
# quotation marks. I fixed it by changing it to "potato",
# so Python recognizes it as a string instead of a variable.


# Section 3.2

numbers = list(range(0, 21))
print(numbers)

def get_first_15(numbers):
    return numbers[0:15]

def get_every_5th(s):
    return s[::5]

def reverse_and_stride(s):
    reversed_list = s[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)


# Section 3.3

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for num in row:
            total += num
    return total

print(sum_nested(numbers))


# Section 3.4

def create_5x5():
    grid = []
    number = 1

    for i in range(5):
        row = []
        for j in range(5):
            row.append(number)
            number += 1
        grid.append(row)

    return grid

grid = create_5x5()
print(grid)


def replace_multiples_of_3(grid):
    for i in range(5):
        for j in range(5):
            if grid[i][j] % 3 == 0:
                grid[i][j] = "?"
    return grid

updated_grid = replace_multiples_of_3(grid)
print(updated_grid)

def sum_grid(grid):
    total = 0

    for row in grid:
        for num in row:
            if num != "?":
                total += num

    return total

grid_total = sum_grid(updated_grid)
print(grid_total)


# Section 4.1

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for name, age in ages.items():
    print(name, age)


# Section 5.2
# This prints the result when running the file in VS Code.

print("Favorite function result:")
print(create_5x5())