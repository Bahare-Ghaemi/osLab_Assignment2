import random

while True:
    print("\nwelcome to the Game...")
    print("1-up")
    print("2-down")
    print("3-exit")

    computer1_choice = random.randint(1,2)
    computer2_choice = random.randint(1,2)
    user_choice = int(input("enter number of your choice : "))

    if user_choice == 3:
        break;

    if computer1_choice == computer2_choice == user_choice:
        print("All of you chose the same! please go on...")

    if computer1_choice == computer2_choice != user_choice:
        print("--- You Lost !!! ---")
        print("Computer1 :",computer1_choice," computer2 :",computer2_choice," you :",user_choice)
    if computer1_choice == user_choice != computer2_choice:
        print("--- Computer2 Lost !!! ---")
        print("Computer1 :",computer1_choice," computer2 :",computer2_choice," you :",user_choice)
    if computer1_choice != user_choice == computer2_choice:
        print("--- Computer1 Lost !!! ---")
        print("Computer1 :",computer1_choice," computer2 :",computer2_choice," you :",user_choice)
    

    
