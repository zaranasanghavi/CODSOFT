import random

def get_system_output():
    return random.choice(["rock", "paper", "scissors"])

def win(input_1, system_output):
    if input_1 == system_output:
        return "Tie 🤖 🟰 😊"
    elif (
        (input_1 == "rock" and system_output == "scissors")
        or (input_1 == "paper" and system_output == "rock")
        or (input_1 == "scissors" and system_output == "paper")
    ):
        return "You WIN!🥳"
    else:
        return "Computer WINS!🤖" 
def get_input_1():
    print("Rock, paper ,scissors or exit")
    input_1 = input().lower()
    if input_1 == "exit":
        return -1
    while input_1 not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        input_1 = input().lower()
    return input_1

def main():
    while True:
        
        
        input_1 = get_input_1()
        system_output = get_system_output()
        
        if input_1 == -1:
            print("Thanks for playing 😊")
            break

        print(f"Your choice {input_1}")
        print(f"Computer's choice {system_output}")

        result = win(input_1, system_output)
        print(result)

if __name__ == "__main__":
    main()