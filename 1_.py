# functions are ways to wrap your code
#into reuseable units
# place ()after the function name to invoke it


# calling
# def happy_bday(name, age):#parameter
#     print(f"happy bday {name}!")
#     print(f"you are {age} years old")
#     print("happy bday!")
# # invoking
# happy_bday("bro", 50)#argument
# happy_bday("friend", 60)

# def display_invoice(username, amount, due_date)
#     print(f"Hello {username},")
#     print(f"your bill of ${amount:.2f} is due on {due_date}")

# #return is a statement used to end a function and send a result to the caller

# def add(x,y):
#     z=x+y
#     return z

# def subtract(x,y):
#     z=x-y
#     return z

# def multiply(x,y):
#     z=x*y
#     return z

# def divide(x,y):
#     z=x/y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Andy", "aranda")

print full_name
