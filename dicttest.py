#re acquainting with dictionairies

dog_0 = {'name': 'lucy', 'age': 12, 'breed': 'labrador', 'color': 'white'}
dog_1 = {'name': 'jasper', 'age': 11, 'breed': 'spinone italiano', 'color': 'cream'}
dog_2 = {'name': 'rudi', 'age': 11, 'breed': 'spinone italiano', 'color': 'cream'}

favorite_toys = {
    'lucy': 'tennis ball',
    'jasper': 'squeaky toy',
    'rudi': 'rope toy'
}

dogs = [dog_0, dog_1, dog_2]
for dog in dogs:
    print(f"\nName: {dog['name'].title()}")
    print(f"Age: {dog['age']}")
    print(f"Breed: {dog['breed'].title()}")
    print(f"Color: {dog['color'].title()}")
    print(f"Favorite Toy: {favorite_toys[dog['name']]}")

for name in favorite_toys:
    print(f"\n{name.title()}'s favorite toy is a {favorite_toys[name]}.")

print("Hare all the toys:")
for toy in favorite_toys.values():
    print(toy)

for dog in dogs:
    print(dog['breed'].title())

breed_choice = input("What is your favorite dog breed? ")
founddog = False
for dog in dogs:
    if dog['breed'] == breed_choice.lower():
        print(f"\n{dog['name'].title()} is a {breed_choice.title()}.")
        founddog = True
if not founddog:
    print(f"\nNo dog of breed {breed_choice.title()} found.")