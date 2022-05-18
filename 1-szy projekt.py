import random

while True:
    my_answer = input("Choose: Rock, Paper or Scissors: ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break
    
    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("Choose correct answer")
        continue

    computer_answer = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The computer choose: {computer_answer}")

    if my_answer == computer_answer:
        print("Draw. Let's play again.")
    elif my_answer == "paper" and computer_answer == "rock":
        print("You win!")
        break
    elif my_answer == "scissors" and computer_answer == "paper":
        print("You win!")
        break
    elif my_answer == "rock" and computer_answer == "scissors":
        print("You win!")
        break
    else:
        print("You lose.")
        