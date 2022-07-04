class Guitar():
  def __init__(self, colour, string_no): # constructor
    self.colour=colour
    self.string_no=string_no
  
  def play(self): # define a method
    print("Noise")



a_guitar=Guitar("Blue", 6) # like (the depreciated) 'new'

print(a_guitar)
print(type(a_guitar))
print(a_guitar.colour)

a_guitar.play()

# all things belong to __main__ object,
#  '__' means 'hidden'






