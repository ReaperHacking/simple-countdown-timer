#Countdown Timer (Seconds)
import time

#Intro
print("Welcome to my countdown timer! \n")
print("Enter an amount of seconds below! \n")

#Input
time_var = int(input("Enter an amount of seconds to countdown from: "))

#Time Function
def time_func():
  time.sleep(time_var)

  print("DONE!")


while time_func() == True:
  #Function
  time_func()

  #Asks user if they would like to restart and conditions
  re_count = input("Would you like to set another time? (Y/N): ").upper()

  if re_count == 'N':
    break
  elif re_count == 'Y':
    continue
  else:
    print("Sorry, error, didn't choose Y or N :/")
    
  
  

