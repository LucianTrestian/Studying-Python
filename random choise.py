from random import *

exit = ""
while exit.lower() != "exit" :
    data = input('Write word with space:').split(" ")
    if data[0].lower() == "exit":
        exit = data[0]
    else:
        print(choice(data))