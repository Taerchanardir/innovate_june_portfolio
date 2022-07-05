from character import Character

print("\n")
print("Spawning a new superhero...")
superhero=Character("Clark Kent", "Superman")

# print(superhero)  this doesn't print the attributes in the object, it just prints what the object type is and it's memory location, unlike print(some_disctionary_object) printing the content of the object

print("Our new hero is:\n")
superhero.print_attributes()

print("\nAdding a superpower...\n")
superhero.set_power("Flying")

superhero.print_attributes()

print("Our superhero's superpower is:\n")

superhero.get_power()

print("")