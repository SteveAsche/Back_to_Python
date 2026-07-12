from restaurant import Restaurant

my_restaurant = Restaurant("Tasty Treats", "Italian", 12, 22)
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(50)
print(f"Number of customers served: {my_restaurant.number_served}")

