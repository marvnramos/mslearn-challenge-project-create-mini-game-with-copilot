

# write an array to store the options rock, paper and scissors
options = ["rock", "paper", "scissors"]

# import the random module
import random

# validate if the user wants to play again using a function and return a boolean
    # write a function to validate the input
def play_again(wins, rounds):
    user_input = input(f"Do you want to play again? (y/n): ").lower()
    if user_input == "y":
        return True, wins, rounds
    elif user_input == "n":
        return False, wins, rounds
    # else, print a message to enter a valid input
    else:
        print("Please enter a valid input")
        return play_again(wins, rounds)


# write a function to get the user choice
def get_user_choice():
    # write a while condition to validate the input
    while True:
        # get the user choice and store it in a variable
        user_choice = input("Enter your choice: ").lower()
        # validate the user choice
        if user_choice in options:
            return user_choice
        # else, print a message to enter a valid input
        else:
            print("Please enter a valid input (rock, paper, scissors)")


# write a function to determine the winner
def determine_winner(user_choice, computer_choice):

    # Check for tie cases
    if user_choice == options[computer_choice]:
        return "It's a tie!"
    
    # Check for user win cases
    if (
        (user_choice == "rock" and options[computer_choice] == "scissors") or
        (user_choice == "paper" and options[computer_choice] == "rock") or
        (user_choice == "scissors" and options[computer_choice] == "paper")
    ):
        return "You won!"
    # return a message if the user lost
    return "You lost!"


# write a function to get a random computer choice
def get_computer_choice():
    # write a random choice for the computer using the random module
    computer_choice = random.randint(0, 2)
    # return the computer choice
    return computer_choice


# write a function play_game
def play_game():
    # call the get_user_choice function and store the result in a variable
    user_choice = get_user_choice()
    # write user choice and computer choice
    print("User choice: " + user_choice)

    # write a variable to stored the computer choice
    computer_choice = get_computer_choice()
    
    # print the computer choice
    print(f"Computer choice: {options[computer_choice]}" )

    # call the determine_winner function and pass the user choice and computer choice as arguments
    result = determine_winner(user_choice, computer_choice)

    # print the result
    return result

    

    
# write a welcome message
print("Welcome to the game app rock, paper, and scissors")

# write a while condition to validate the input
# write a variable to store the boolean value
flag = True
# write a variable to store the number of wins
wins = 0
# write a variable to store the number of rounds
rounds = 0
while flag:
    # call the play_game function and store the result in a variable
    result = play_game()
    # print the result
    print(result)
    # increment the number of rounds
    rounds += 1
    # increment the number of wins if the user won
    if(result == "You won!"):
        wins += 1
    # call the play_again function and store the result in a variable
    flag, wins, rounds = play_again(wins, rounds)

print(f"Thanks for playing! You won {wins} out of {rounds} rounds.")
        
        
        

    

