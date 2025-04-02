# function is a block of reusable code
# place ()after function to evoke it


# def happy_song(name,age):
#     print(f"happy birthday to {name}")
#     print(f"wow you are{age}")
#     print("happy birthday to you")
#     print()
# happy_song("kuku",12)
# happy_song("fafa",20)
# happy_song("luvy",20)

# def display_invoice(username,amount,due_date):
#     print(f"helo {username}")
#     print(f"you bill is {amount} and is due on{due_date}")

# display_invoice("pure",5,"10/12")

# RETURN function = statement used to end a fuction and 
# send results back to the caaller

# def create_name(first , last):
#      first= first.capitalize()
#      last= last.capitalize()
#      return first + " " + last
# full_name = create_name("precious","mutema")

# print(full_name)



def greet(name):
    print (f"hello!{name} welcome to python")
greet("precious")
greet("anna")

def add (a,b):
    return a+b
result=add(4,8)
print(result)

def greet (name="guest"):
    print(f"hello,{name}")
greet()

def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")
    inner()
outer()

    














