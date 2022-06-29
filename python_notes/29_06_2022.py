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


