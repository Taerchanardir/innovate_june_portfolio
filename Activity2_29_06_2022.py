countries={
  "The United Kingdom":"London",
  "France":"Paris",
  "Germany":"Berlin",
  "Spain":"Madrid",
  "Italy":"Rome"
}

countries.setdefault("Ireland","Dublin")
countries.setdefault("Switzerland","Bern")

# print(countries) ## could do this, but it's a bit untidy and shows all the formatting {'s and :'s and ,'s

print("")

for key in countries.keys():
  print(f"The capital of {key} is {countries[key]}")
  ## but this is neater

print("")

try:
  countries.update({"The United Kingdom":"English"})
  countries.update({"France":"French"})
  countries.update({"Germany":"German"})
  countries.update({"Spain":"Spanish"})
  countries.update({"Italy":"Italian"})
  countries.update({"Ireland":"English"})
  countries.update({"Switzerland":"French and German"})


  for key in countries.keys():
    print(f"The language spoken in {key} is {countries[key]}")

except:
  print("There is a typo in the code!")

