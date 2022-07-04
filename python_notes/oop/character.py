class Character():
  def __init__(self, real_name, superhero_name):
    self.real_name = real_name
    self.superhero_name = superhero_name
    self.power="Nothing yet"

  def set_power(self, power):
    self.power = power

  def get_power(self):
    print(self.power)

  def print_attributes(self):
    print("Real name: "+self.real_name +"\nSuperhero name: "+self.superhero_name) #+"\n")
    if(self.power!=None):
      print("Superpower: "+self.power+" \n")

