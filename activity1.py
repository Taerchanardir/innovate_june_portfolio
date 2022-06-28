#activity 1
# is the function just supposed to check if the length is even, or to do the whole check and print?
# we have not yet done 'return', so it all has to be done in the one function...
# the function could find the length too, to save passing it as an argument, but that isn't what the first part of the activity says (thinking of trick wording in exams here).

def check_and_print(string_arg, length_arg):
  message1=string_arg+" is "+str(length_arg)+" characters long"
  #print(type(string_length)) # and now it actually is an int...
  if length_arg%2 == 0: # True if even
    print(f"{message1}, it is an even length")
  else:
    print(f"{message1}, it is an odd length")


the_string = "Welcome to CodeNation."
string_length=len(the_string)
check_and_print(the_string, string_length)


