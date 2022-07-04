class Person():         # convention: capitalise class names
  def __init__(self, person_name, person_age, person_height):   # define the constructor. sets attributes. looks like 'self' is not implicit in the way 'this' is
    # self.name=None    # self == this
    self.name = person_name
    # self.name = name  # usually do it this way
    # self.another_attribute = 1234
    self.age = person_age
    self.height = person_height

  def set_hair(self, person_hair): # a setter
    self.hair = person_hair

  def get_hair(self):
    print(self.hair)
    #return self.hair







# me = Person("Eric",55)
# metoo = Person("Ernie",103)

# print(me.name)
# print(metoo.name)
# print(me.another_attribute)

