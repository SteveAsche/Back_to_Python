#relearning if statements
old_cars = ['chevy', 'ford', 'dodge', 'pontiac']
my_car = 'chevy'
if my_car not in old_cars:
    print(f"{my_car.title()} is not an old car.")
else:
    print(f"{my_car.title()} is an old car.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'french fries', 'olives']
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")
            
print("\nFinished making your pizza!")