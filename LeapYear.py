#Receive year as user input
year = int(input("Which year do you want to check? "))

#Perform calculation to determine if year is a leap year or not.
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    isLeap = True
elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    isLeap = True
else:
    isLeap = False

if isLeap == True:
    print(f"{year} is a leap year.") # Leap year.
else:
    print(f"{year} is not a leap year.") #Not leap year