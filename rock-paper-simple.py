import random

(
    LOSE,
    WIN,
    DRAW,
    UNDECIDED
) = range(4)

def main():
    print("ROCK, PAPER, SCISSORS")

    while True:
        print("Make your move! Type \"exit\" or \"quit\", and then press the Enter key, to terminate the program.")
        user_input = input("Rock, paper, scissors: ")
        user_input = user_input.strip().lower()

        if user_input == "exit" or user_input == "quit":
            break

        if user_input != "rock" and user_input != "paper" and user_input != "scissors":
            try:
                user_input = int(user_input)

                if user_input == 1:
                    user_input = "rock"
                elif user_input == 2:
                    user_input = "paper"
                elif user_input == 3:
                    user_input = "scissors"
            except ValueError:
                print("Input value could not be interpretted. Please try again.")
                break

        player_state = UNDECIDED

        # generate a random selection for the NPC
        npc_selection = random.choice(["rock", "paper", "scissors"])

        if user_input == "rock":
            if npc_selection == "rock":
                player_state = DRAW
            elif npc_selection == "paper":
                player_state = LOSE
            elif npc_selection == "scissors":
                player_state = WIN
        elif user_input == "paper":
            if npc_selection == "rock":
                player_state = WIN
            elif npc_selection == "paper":
                player_state = DRAW
            elif npc_selection == "scissors":
                player_state = LOSE
        elif user_input == "scissors":
            if npc_selection == "rock":
                player_state == LOSE
            elif npc_selection == "paper":
                player_state == WIN
            elif npc_selection == "scissors":
                player_state = DRAW
        
        print(f"You chose {user_input}. The NPC chose {npc_selection}.")

        if player_state == WIN:
            print("You won!\n")
        elif player_state == LOSE:
            print("You lost...\n")
        else:
            print("Draw!\n")

    print("Thank you for playing! The program is terminating.")

if __name__ == "__main__":
    main()
