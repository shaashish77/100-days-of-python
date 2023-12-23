# control flow 
# if Condition 
#  do This 
# else :
#     do this

# nested if else
# if Condition 
#  do This 
#   if 
# else :
#     do this

# program ***********

# print("Welcome To The Rollercoaster!")

# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can Enjoy the rollercoaster! yay!")
# else:
#     print("Sorry you cannot ride the rollercoaster")


# program Nested if else **************

print("Welcome To The Rollercoaster!") 

height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
bill = 0
if height >= 120:
    print("You can Enjoy the rollercoaster! yay!")
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <=18:
        bill = 7
        print("Please pay $7")
    else:
        print("Please pay $12.")
        bill = 12
    wants_photo =input("Do you want a photo taken? Y or N :")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final Bill is {bill}")
else:
    print("Sorry you cannot ride the rollercoaster")