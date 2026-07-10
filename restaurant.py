# playing with classes and objects

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, opening_time, closing_time):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.opening_time = opening_time
        self.closing_time = closing_time


    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is now open!")

    def are_they_open(self, current_time):
        """Check if the restaurant is open based on the current time."""
        if self.opening_time <= current_time < self.closing_time:
            print(f"{self.restaurant_name} is currently open.")
        else:
            print(f"{self.restaurant_name} is currently closed.")

Max = Restaurant('Max', 'Italian', 11, 22)
Albertos = Restaurant('Albertos', 'Mexican', 10, 23)
Sidetracks = Restaurant('Sidetracks', 'American', 9, 21)
Baci = Restaurant('Baci', 'Italian', 12, 23)
Haps = Restaurant('Haps', 'American', 11, 22)

Haps.are_they_open(12)  # Check if Haps is open at 12 PM
