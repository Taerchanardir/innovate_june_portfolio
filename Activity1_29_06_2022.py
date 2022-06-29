retry=True

while(retry):
  userstring=input("Enter an integer: ")
  try:
    retry=False
    userint=int(userstring)
  except:
    print("Please try again, That input was not convertible to an int")
    retry=True

print(f"Your integer was {userint} and was type {type(userint)}")



  



