# functions with 0utput
# def format_name(f_name, l_name):
#     format_n= (f_name.title())
#     format_l= (l_name.title())
#     return f"{format_n} {format_l}"
    # print("SAh")  not reachable
    
# print(format_name("asHish", "sah"))

# multiple return statements

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
     return "Nothing"
    format_n= (f_name.title())
    format_l= (l_name.title())
    return f" Result: {format_n} {format_l}"

print(format_name(input("What is your 1st name?"), input("What is your lst name?")))

