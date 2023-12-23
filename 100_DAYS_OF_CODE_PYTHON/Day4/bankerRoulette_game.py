import random

name_string = input("Give me everybody's names, seperated by a comma. ")

names = name_string.split(", ")

num_items =len(names)

random_choice =random.randint(0, num_items-1)

person_who_pays = names[random_choice]

print(person_who_pays + " is going to pay the bill. Yay!")