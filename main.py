from os import system
import random

# Symbols & Numbers & Characters
high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = high.lower()
numbers = "1234567890"
Symbol = "!$%&^@"

all = high + low + numbers + Symbol

# Create Function
def Generator():
    # How Much Length Password ? \/
    length = int(input("Enter Length Your Password : "))
    
    # Your Password
    Password = ""
    
    # Loop
    for i in range(length):
        num =  random.randrange(0,len(all))
        Password += all[num]
    
    # Result Password !
    print("Result Password : " + str(Password))
    
    # Generator Password Again ?
    print("\nGenerator Password Again ?\n")
    
    # Type Y Or N
    x = input("Yas / No [y/n] : ")
    
    if x.lower() == "y":
        system("cls") # Clear Console
        Generator()
    elif x.lower() == "n":
        exit()
    else :
        print("This Command is Not Here : " + x)


Generator()