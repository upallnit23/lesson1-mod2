import datetime
import math

#Decisions at the Crossroads

#Task 1: Code Correction

number = int(input("Enter a number"))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#2. The Story Brancher
    
#Task 1: Code Correction
    
choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

# The Greatest Showdown
    
#Task 1: Identify the Greatest
    
num1 = int(input("Enter a number" ))
num2 = int(input("Enter a second number" ))
num3 = int(input("Enter a third number" ))

if (num1 > num2) and (num1 > num3):
    print(num1, " is the largest of the three numbers.")
elif (num2 > num1) and (num2 > num3):
    print(num2, "is the largest of the three numbers.")
elif (num3 > num1) and (num3 > num2):
    print(num3, "is the largest of the three numbers.")
#else:
#    print("At least 2 numbers are the same.")

if (num1 < num2) and (num1 < num3):
    print(num1, " is the smallest of the three numbers.")
elif (num2 < num1) and (num2 < num3):
    print(num2, "is the smallest of the three numbers.")
elif (num3 < num1) and (num3 < num2):
    print(num3, "is the smallest of the three numbers.")
#else:
#    print("At least 2 numbers are the same.")

if (num1 == num2) and (num1 == num3):
    print("All numbers are equal.")
elif (num1 == num2):
    if (num1 > num3):
        print(num1, num2, " are the largest numbers, and are the same.")
    else:
        print(num3, " is the largest number")
elif (num2 == num3):
    if (num2 > num1):
        print(num2, num3, " are the largest numbers, and are the same.")
    else:
        print(num1, " is the largest number")
elif (num1 == num3):
    if (num1 > num2):
        print(num1, num3, " are the largest numbers, and are the same.")
    else:
        print(num2, " is the largest number")
else:
    print("Numbers are all different.")

#Leap Year Explorer
    
#Task 1: Leap Year Checker
    
user_date = datetime.datetime.now()
#print(user_date)
#print(user_date.year)
#print(user_date.strftime("%Y"))

user_year = int(input("Enter a year"))

if (user_year % 100 == 0) and (user_year % 400 != 0):
    print("This is a skipped leap year!")
elif (user_year % 4 == 0):
    print("This is a leap year!")
else:
    print("This is not a leap year.")

#Task 2:Century Verification

if user_year % 1000 == 0:
    print("This is a century year.")
else:
    print("This is not a century year.")

#Task 3: Time Traveler
    
if user_year > user_date.year:
    print("This year is in the future!")
elif user_year == user_date.year:
    print("This year is current!")
elif user_year < user_date.year:
    print("This year is in the past!")
else:
    print("This year is strange.")



