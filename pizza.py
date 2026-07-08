# simple pizza.py   
pizzas = ["pepperoni", "mushrooms", "green peppers", "extra cheese"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

fibonacci_numbers = []
first_number = 0
second_number = 1
index = 0
while index < 20:
    fibonacci_numbers.append(first_number)
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
    index += 1

print(fibonacci_numbers)


cubes = [value ** 3 for value in range(1, 11)]
print(cubes)    


buffet = ("pizza", "pasta", "salad", "soup", "breadsticks")
for food in buffet:
    print(food)

#buffet[0] = "ice cream"  # This will raise an error because tuples are immutable
