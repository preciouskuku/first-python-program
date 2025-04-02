# while loops =execute some codes while he condition remains True

# name= input("enter your name: ")
# while name=="":
#     print(f"you did not enter your name : ")
#     name= input("enter your name: ")
# print(f"hello {name}")


# age = int(input("how old are you ? "))

# while age <=0 :
#     print ("your age is invalid")
#     age = int(input("how old are you ? "))
# print(f"{age} thats old")

# food = input("Enter the food you like (q to quit): ")

# while not food == "q" :
#     print(f"you like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye food lover ")
# help=input("enter a command: ")
# start=input("enter a command: ")
# stop=input("enter a command: ")
# quit=input("enter a command: ")

# game=input("enter a command: ")
# while game ==help:                                                                                                                                                      


# num = int(input("Enter a number between 1 and 10 : "))

# while num <1 or num >10 :
#     print(f"{num} is invalid")
#     num = int(input("Enter a number between 1 and 10 : "))

# print(f"{num} entered is successful")
 
# num =int(input("guess the number : "))  
# while num >7 or num<7:
#     print("wrong number")
#     num =int(input("guess the number : ")) 
# print("correct number")


# FOR LOOPS
# execute a block of codes at a fixed number of times you can literate over a range,string and sequence etc
# for loops is used to literate over sequence

# SYNTHAX :
# For variable in sequence

# fruits = ["a","B","c"]
# for fruits in fruits:
#     print(fruits)


# text="python"
# for char in text:
#     print(char)


# for x in range (1,11) :
#     print(x)

# for count_down in reversed(range (1,11)) :
#     print(count_down)
# print("Happy new year")


# i=10
# while i > 0:
#     print(i)
#     i -= 1

# credit_card ="1234-5678-9012"

# for x in credit_card:
#     print(x)

# for x in range (1,50,5) :
#     if x ==18 :
#      continue

#     else:
#        print(x)
# for x in range (1,22) :
#     if x ==18 :
#      break
#     else:
#        print(x)


#        NESTED LOOPS
# is a loop in another loop
# for y in range (3):
#     for x in range (1,11):
#         print( x , end = "")
#     print()

# rows=int(input("Enter the # of rows: "))
# columns=int(input("Enter the # of columns: "))
# symbol=input("Enter the # of symbol: ")

# for x in range (rows):
#     for x in range (columns):
#         print( symbol , end = "")
#     print()


#     # WHILE True IS USED TO EXECUTE a code when you want to break the loop

# command =input("enter the command : ")
# help={"start":"to start car","stop":"to stop car","quit":"to exit"}


# command =input("enter the command : ")

# while True :
#     if command=="help":
#         print(help)
#         command =input("enter the command : ")
#     elif command=="start":
#         print("car started")
#         command =input("enter the command : ")
#     elif command=="stop":
#         print("car stoped")
#         command =input("enter the command : ")
#     elif command=="quit": 
#         print("exit the game")
#         break
#     else:
#         print("i dont understand this")
#         command =input("enter the command : ")
