#start wiht unconfirmed users

unconfirmed_users = [
    'alice',
    'brian',
    'candace',
]
confirmed_users = []


#verify each user until there are no more unconfirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(len(confirmed_users))

#pet test
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'cat', 'dog', 'dog']
print (pets)

while 'cat' in pets:
    pets.remove('cat')  
print(pets)
