# Review
# def greet():
#     print("Hi")
#     print("Hi")
#     print("Hi")

# greet()

# function with input

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Ashish")

# function with more input
def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")
greet_with("Ashish", "India")

# or

def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")
greet_with(name="Ashish", location="India")
# or
greet_with(location="India", name="Ashish")