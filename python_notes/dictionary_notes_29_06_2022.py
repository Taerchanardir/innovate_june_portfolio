import random

# light = False
# def light_switch():
#     global light            #  and with this line (added afterwards) it forces it to be global
#     if light:               # if you comment out the 2 assignments below, this var is assumed to be the global variable and works, but if the 2 assignemnts below are there, it assumes this is a local variable and errors. Odd behaviour coming from C/C++
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()

# # or you could just not hide global variables by using the same name in a function...... g_variable_name etc
# # globals are considered generally bad, bad idea to set them in functions, make them read only


# # list
# evens=[2,4,6,8,10]   # mutable, can be changed
# evens.append(12)
# evens.insert(0,0)
# print(evens)

# # tuple   
# odds=(1,3,5,7,9)     # immutable / const, can't be changed
# #odds.append()    # nope. has no methods for changing entries
# print(odds)

# fav_games=[
#   "Robotron",
#   "Elder Scrolls Online",
#   "Minecraft"
# ]

# fav_songs = [
#   "Yes - Close to the Edge",
#   "Beethoven - 9th",
#   "C419 - That song with the filtery synth that keeps endlessly repeating in Minecraft"
# ]


# # slices
# # start:stop:step
# print(fav_songs[1:1:1])
# print(fav_songs[1:2:1])

# #[1] just one index position
# #[1:] all, assuming the rest to be 'end' and '1'
# print(fav_songs[1])       # prints single entry
# print(fav_songs[1:2:1])   # prints sinlge entry, but with the enclosing ['    ']


# #test="Hello"
# test="qwertytrewq"

# #if(test.__reversed__() == test):   # popup suggested __reverse__ but it doesn't exist
# if test==test[::-1]: # this must intelligently assume we are starting at the end of the string because of the -1 step
#   print(f"'{test}' is palindrome")
# else:
#   print(f"'{test}' isn't palindrome")  


# # continue/break
# num=random.randint(1,50)
# while num%2==0:
#     print("We like even numbers! Another!")
#     num=random.randint(1,50)

# print("Oh no! An odd number!")

# # solves the 'setting the loop condition variable an extra time before the loop' problem
# while True:
#     num=random.randint(1,50)
#     print(num)
#     if num%2==0:
#         print("We like even numbers! Another!")
#         continue  # continue the loop from the while
#     else:
#         print("An odd number!")
#         break     # exit the loop



# Dictonaries

# not ordered, {} define variable as being a dictionary

#a_list=["one","two","three"]

#dictionary uses key:value pairs
# key has to be hashable string or int
#my_cat={
#  "name":"Salem",  # name is key, Salem is value
#  "colour":"Black"
#}
#
#key must be unique


my_imaginary_cat={
  "name":"Spot",
  "breed":"Fluffy",
  "mood":"I want food!"
}

# # dictionaries do not have a numbered index. can't do
# # print(my_imaginary_cat[1])   # key error

# print(my_imaginary_cat["name"])

# print(f'My imaginary cat {my_imaginary_cat["name"]} is a bit {my_imaginary_cat["mood"]} today')

#change a value using a key:
#my_imaginary_cat["mood"] = "sleepy"


# print(my_imaginary_cat.keys())
# = dict_keys(['name', 'breed', 'mood'])

x=my_imaginary_cat.keys()

my_imaginary_cat["age"]=2

print(x)
# x is a sort-of reference...but only to the 'keys' part, not the values in the dictionary....depends on how dictionaries work in the background
# called a 'view object'

v=my_imaginary_cat.values()
print(v)

ii=my_imaginary_cat.items() # gives (reference to) the key:value pairs
print(ii)



print(my_imaginary_cat.get("mood"))  # same as [] method


print(my_imaginary_cat.get("legs"))
print(my_imaginary_cat.get("legs","key 'legs' does not exist"))

#print(my_imaginary_cat["legs"])

print(list(my_imaginary_cat.keys()))

for i in list(my_imaginary_cat.keys()):
  print(i)

for i in my_imaginary_cat.keys():
  print(i)

my_imaginary_cat.update({"legs":"4"}) # update, like append. add new key
print(my_imaginary_cat)
my_imaginary_cat.update({"name":"Rover"}) # change an existing key
print(my_imaginary_cat)
my_imaginary_cat.pop("mood")
print(my_imaginary_cat)

















