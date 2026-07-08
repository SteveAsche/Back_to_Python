#just a first one
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
bicycles[2] = "bianchi"
print(bicycles[2].title())
bicycles.append("huffy")
print(bicycles)
bicycles.insert(1, "schwinn")
print(bicycles)
popped_bike = bicycles.pop()
print(popped_bike)
bicycles.remove("cannondale")
print(bicycles)
bicycles.sort()
print(bicycles)
for bike in bicycles:
    print(bike.title())
print("\n")
print("thqt was a nice list of bikes")
