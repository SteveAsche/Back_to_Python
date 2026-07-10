# various application for functions

def display_message():
    """Display a simple message."""
    print("Hello! This is a function that displays a message.")

def favorite_book(title):
    """Display a message about favorite book."""
    print(f"One of my favorite books is {title.title()}.")


display_message()
favorite_book("The Great Gatsby")

#positional arguments
def describe_pet(animal_type='dog', pet_name='duke'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='bane', animal_type='cat')  # keyword argument
describe_pet(pet_name='shadow')  # default value for animal_type
describe_pet()  # default values for both animal_type and pet_name
