import random

# from random import random, randint, uniform
# then 'print(uniform(0,10))' etc, omitting 'random.'   a bit like 'using' with namespaces

# greeting="Hello Everyone!"
# print(len(greeting))
# print(greeting[1])
# # print("1234"+1)     # nope, as expected, can only join strings
# print(greeting[-1])   # counting from end of string
# print(greeting.upper())
# print(greeting.count("e"))  # 4
# print(greeting.lower())

# print(greeting.casefold())  # nothing visible
# print(greeting.center(20))  
# print(greeting.find("l"))   # 2
# ss="The quick brown fox"
# print(ss.replace("fox","cat")) # should be quick > lazy
# print("              some typing  ".strip())
# print(len("the quick brown fox                                  ".strip()))
# print(ss.strip("The quick"))
# print(ss.strip("brown"))   # does nothing, but also throws no error

# print(random.random())        # probably exclusive / not including 1.0

# print(random.uniform(0,10))   # is end exclusive ?

# print(random.randint(1,10))   # beware, end is inclusive

# my_name="Eric"
# my_age=306
# print(my_name, my_age)
# print("Hello his name is",my_name)
# print("Hello my name is "+my_name)
# #print("I am" + my_age) # nope
# print("I am "+str(my_age))
# print(f"I am {my_age}") # without the 'f' the {my_age} is just treated as a string. 'f' means 'format' ?

# print("Hello my name is {} and I am {} years old".format(my_name, my_age)) # the alternate way, a bit closer to C/C++
# print(f"Hello my name is {my_name} and I am {my_age} years old")            # easier to read, more editing to swap vars around.  So how to subst in an array of things?
# # 'f' method is apparently new best practice. Coding languages have fashions

# # ** means ^, exponent, and not 'pointer to pointer' etc
# print(3**3)
# print(15%3)    # modulus, gives an int,  =0
# print(301/21)  # gives a float
# balance=100
# amount=20
# balance+=20    # yes, python does have (whatever this type of operator is called)
# print(balance)

# answer=input("What is your name? ") # always a string input. needs a space if on same line or is looks messy
# print(answer)

# answer=input("What is your name?\n")  # input blocks of course. Can we do threads in python?, or async function calls that 'return' an event later whilst the thread continues?
# print(answer)


# #if something_variable == some_other_variable:   # the : is equivalent to { in C++
#   # do something                                 # needs indents. python works by indents and not curly brackets. if block is ended by ending indentation, not the elif
# #elif something_else == another_variable:
#   # do something else 
# #else:

# music = "Classical"

# if music.tolower() == "classical":
# # or music=music.tolower()     # presume a non-indented comment doesn't end the block  
#   print("something")
# elif(music == "nothing"):
#   print("another comment")
# else:
#   # catches everything else

# # elif ends with end of indentation

# print(10%3==0) False

# num=10
# num2=20
# if num > num2:
#   print(f"{num} is bigger than {num2}")
# elif num2 > num:
#   print(f"{num2} is bigger than {num}")
# else:
#   print(f"{num} is same as {num2}")

# place="MCR"
# weather="Cloudy"
# if place=="MCR" and weather == "Sunny":
#   print("The moors are probably on fire again")
# elif place=="MCR" and weather=="Rain":
#   print("All is normal")
# else:
#   print("Not MCR, or it is just cloudy, which is also normal")
# # coming soon, operator precedence, and swathes of ((('s


# day = "Monday"
# bank_hol = True
# if day == "Saturday" or day == "Sunday" or bank_hol:
#   print("A day off")
# else:
#   print("It isn't the weekend")


# Functions

# # like lua and languages that run the whole file from top to bottom, functions are skipped past
# # 'def' and : and indentation define a function and it's body
# def light_switch():
#   print("Blurb")

# light_switch()

# def withdrawal(amount, account):
#   print(f"Withdrawing {amount} from account {account}")

# withdrawal(300, 123456)  


# Lists:

# fave_songs = [
#   "Yes - Close to the Edge",
#   "Beethoven - 9th",
#   "C419 - That song with the filtery synth that keeps endlessly repeating in Minecraft"
# ]

# print(fave_songs) # prints whole list/object, including the ['s and commas between items

# fav_games=[
#   "Robotron",
#   "Elder Scrolls Online",
#   "Minecraft"
# ]

# # # print(fav_games[0])

# # #print(fav_games)
# # # fav_games[1]="Skyrim"
# # #print(fav_games)
# # print(len(fav_games))
# # fav_games.append("Coding addons") # add item to end
# # print(fav_games)
# # fav_games.pop() # pop and return the last item from list, as if list was a stack. an index position can be given
# # print(fav_games)
# # # fav_games.insert exists, .push() does not

# # for i in fav_games: # i iterates through all things in list, in this case strings. it is not the numeric index of the entry in the list
# #   print(i)

# # for i in range(10):    # 0 to 9
# #   print(i)
# # for i in range(4,10):  # 4 to 9
# #   print(i)
# # for i in range(3,10,2): # 3 to 9 in steps of 2
# #   print(i)

# for i in range(10,-1,-1):
#   print(i)


my_num=random.randint(0,40)
random_numb=random.randint(0,40)
while random_numb!=my_num:
  print(f"{random_numb} does not match {my_num}")
  random_numb=random.randint(0,40)
print(f"{random_numb} does match {my_num}")


