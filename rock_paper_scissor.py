import random

game = ["rock","paper","scissor"]
quit = False
user_score = 0
comp_score = 0
while(user_score < 5 and comp_score < 5 and not quit):
    user_input = input("Enter (rock,paper,scissor): ")
    if (user_input != "rock" and user_input != "paper" and user_input != "scissor"):
        print("Please enter valid input...")
        continue
    comp_input = game[random.randint(0,len(game)-1)]
    print(f"Computer's choice: {comp_input}")
    if(user_input == "rock" and comp_input == "scissor"):
        user_score += 1
    elif(user_input == "paper" and comp_input == "rock"):
        user_score += 1
    elif(user_input == "scissor" and comp_input == "paper"):
        user_score += 1
    elif(user_input == "quit"):
        quit = True
    elif(user_input == comp_input):
        continue
    else:
        comp_score += 1

print(f"Your Score: {user_score}")
print(f"Computer Score: {comp_score}")
