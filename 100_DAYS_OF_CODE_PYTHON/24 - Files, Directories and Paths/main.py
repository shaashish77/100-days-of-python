# one way
# file = open('my_text.txt')
# content = file.read()
# print(content)
# file.close()

# another way
# with open('my_text.txt') as file:
#     content = file.read()
#     print(content)

with open('file_me.txt', mode='a') as file:
    file.write("Hi, babe hamar nishu")

