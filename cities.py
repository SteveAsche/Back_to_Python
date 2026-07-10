prompt = "\nPlease enter the nae of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


newprompt = "\nWhat pizza toppings would you like? "
newprompt += "\n(Enter 'quit' when you are finished.) "
pizza_toppings = ["pepperoni", "mushrooms", "green peppers", "extra cheese", "sausage", "bacon", "pineapple", "spinach", "onions", "olives"]
pizza = []

while True:
    topping = input(newprompt)

    if topping == 'quit':
        break
    else:
        if topping in pizza_toppings:
            print(f"{topping.title()} is added to the pizza.")
            pizza.append(topping)
        else:
            print(f"{topping.title()} is not available as a topping.")

print("\nYour pizza will have the following toppings:")
for topping in pizza:
    print(f"- {topping.title()}")
            