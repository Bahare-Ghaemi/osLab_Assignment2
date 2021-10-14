import random

computer_point = 0
user_point = 0

while True:

    print("\nwelcome to the Game...")
    print("1-stone")
    print("2-paper")
    print("3-scissor")
    print("4-exit")

    computer_choice = random.randint(1,3)
    user_choice = int(input("enter number of your choice : "))

    if computer_choice == user_choice:
        print("you and computer chose the same! please go on...")

    if user_choice == 4:
        break;
    
    if computer_choice == 1 and user_choice == 3:
        computer_point +=1
        print("one point for computer!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if computer_point == 5:
            print("--- you lost !!! ---")
            break

    if computer_choice == 3 and user_choice == 1:
        user_point +=1
        print("one point for you!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if user_point == 5:
            print("*** you wiiiiiiiin !!! ***")
            break

    if computer_choice == 1 and user_choice == 2:
        user_point +=1
        print("one point for you!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if user_point == 5:
            print("*** you wiiiiiiiin !!! ***")
            break

    if computer_choice == 2 and user_choice == 1:
        computer_point +=1
        print("one point for computer!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if computer_point == 5:
            print("--- you lost !!! ---")
            break

    if computer_choice == 2 and user_choice == 3:
        user_point +=1
        print("one point for you!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if user_point == 5:
            print("*** you wiiiiiiiin !!! ***")
            break

    if computer_choice == 3 and user_choice == 2:
        computer_point +=1
        print("one point for computer!"," computer choice : ",computer_choice)
        print("user :",user_point," ***  computer : ",computer_point)
        if computer_point == 5:
            print("--- you lost !!! ---")
            break

        
        

            
        

