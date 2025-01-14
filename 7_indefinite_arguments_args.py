# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
def display_name(*args):
#     for arg in args:
#         print(arg, end="-")

# display_name("Dr.", "spongebob", "Harold", "Squarepants", "III")

# def print_adress(**kwargs):
#     for value in kwargs.values():
#         print(value)

# print_adress(street="123 Fake St.", apt="100", city= 'The raq', state="Illinois", zipcode="60638")

def shipping_label(*args, **kwargs):
    pass
    for arg in args: 
    print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
shipping_label("Dr.", "Spongebob", "squarepants", "III", street="123 Fake St.", apt="100", city= 'The raq', state="Illinois", zipcode="60638" )