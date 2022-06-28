#activity 1
# is the function just supposed to check if the length is even, or to do the whole check and print?
# we have not yet done 'return', so it all has to be done in the one function...
# the function could find the length too, to save passing it as an argument.

def check_and_print(the_string, string_length):
  message1=the_string+" is "+str(string_length)+" characters long"
  #print(type(string_length)) # and now it actually is an int...
  if string_length%2 == 0: # True if even
    print(f"{message1}, it is an even length")
  else:
    print(f"{message1}, it is an odd length")


the_string = "Welcome to CodeNation."

string_length=len(the_string)

check_and_print(the_string, string_length)


