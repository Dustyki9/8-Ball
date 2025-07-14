print("Welcome to the 8 Ball!")

import random

# List of possible Magic 8 Ball responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


# Function to randomly select a response
def magic_8_ball():
    return random.choice(responses)


play = input("Do you want to ask the Magic 8 Ball a question? (yes/no): ").strip().lower()

while play != 'yes':
    print("Okay, maybe next time!")
    play = input("Do you want to ask the Magic 8 Ball a question now? (yes/no): ").strip().lower()


while True:
    user_input = input("Please ask a question (or type 'exit' to quit): ").strip().lower()

    if user_input == "exit":
        print("Thanks for playing! Goodbye!")
        break  # Exit condition checked after loop body has started — simulating a posttest loop
    elif user_input == "":
        print("You didn't ask a question. Please try again.")
    else:
        print(magic_8_ball())


