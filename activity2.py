# activity 2


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for letter in alpha:
  print(letter)

userinput=int(input("Please enter a number from 1 to 26\n?"))
userinput-=1
if userinput < 0 or userinput >= len(alpha):
  print("That number is out of range!")
else:
  print(f"number {userinput+1} represents letter {alpha[userinput]}")

