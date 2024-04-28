
print("Welcome!")
def findpi():
  try:
    inputnumber=int(input("Please enter a number to estimate the digits of PI:"))
    pi = 0
    for n in range (inputnumber):
      value = ((-1)**n)/(2*n+1)
      pi = pi + value
      n = n+1
    pi = pi*4
    return ("Your estimated value of PI is: \n" + str(pi))
  except:
    return("Error! \nPlease enter a positive whole number. \nLetters or words, negative numbers and decimals are not allowed.")
result=findpi()
print (result)


