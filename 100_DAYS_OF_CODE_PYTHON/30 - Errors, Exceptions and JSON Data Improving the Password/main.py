# Errors
# File not found
# with open ("A_file.txt") as file:
#     file.read()

#  key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existence_key"]

# index error
# lista = ["Apple"]
# lista = lista[1]

# type error
# sexy = "abc"
# print(sexy + 5)

# error handling

# try= something that might cause an exception,
# except = do this if there were no exceptions,
# else= do this if there were no exceptions,
# finally = do this no matter what happens.

# let's do this
# try:
#     file = open("a_text.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["as aas"])
# except FileNotFoundError:
#     file = open("a_text.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} no exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Here we are i made it up")

# raising own exceptions

# height = float(input("height: "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("Should not be greater than 3 meters")
# bmi = weight / height ** 2
# print(bmi)
