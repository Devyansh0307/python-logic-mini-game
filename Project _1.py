import random

'''
1 for snake
-1 for water
0 for gun
'''

def get_computer_choice():
    return random.choice([-1, 0, 1])

def get_user_choice():
    while True:
        user_input = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
        if user_input in ['s', 'w', 'g']:
            return user_input
        else:
            print("Invalid input. Please try again.")

def determine_winner(computer, you):
    if computer == you:
        return "Draw"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        return "You won"
    else:
        return "You lose"

def play_game():
    computer = get_computer_choice()
    user_input = get_user_choice()
    choice_dict = {"s": 1, "w": -1, "g": 0}
    you = choice_dict[user_input]
    
    print(f"Computer chose: {['water', 'gun', 'snake'][computer + 1]}")
    print(f"You chose: {['water', 'gun', 'snake'][you + 1]}")
    
    result = determine_winner(computer, you)
    print(result)

if __name__ == "__main__":
    play_game()