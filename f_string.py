person = "Amey"
coins = 5

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins )
print(message)

message = "\n{} has {} coins left." .format(person, coins )
print(message)

message = "\n{1} has {0} coins left." .format(coins, person)
print(message)

message = "\n{person} has {coins} coins left." .format(coins = coins, person = person)
print(message)

player = {'person': 'Amey', 'coins': 6}

message = "\n{person} has {coins} coins left." .format(**player)
print(message)



############################
# f-strings ! this is the way 

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {2*6} coins left."
print(message)