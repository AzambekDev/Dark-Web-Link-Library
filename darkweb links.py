import random

print("Welcome to DWLL or Dark Web Links Library. with over a thousand\n links you can find anything you desire just type: random\n creator:itszxiety\n DISCLAIMOR: LINKS MAYBE BE LEADING TO ILLEGAL WEBSITES USE AT YOUR OWN RISK!!!\n")

# Read the external list from a file
with open("python\external_list.txt", "r") as file:
    external_list = [line.strip() for line in file]

while True:
    user_input = input("Type 'random' to get a result or 'exit' to quit: ")
    
    if user_input.lower() == "random":
            if external_list:
                random_item = random.choice(external_list)
                print("Randomized result:", random_item)
            else:
                print("The list is empty.")
    elif user_input.lower() == "exit":
        break
    else:
        print("Invalid input. Type 'random' to get a result or 'exit' to quit.")
        


