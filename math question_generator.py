import random

OPERATIONS = {
    "1": ("+", lambda a, b: a + b),
    "2": ("-", lambda a, b: a - b),
    "3": ("*", lambda a, b: a * b),
    "4": ("/", lambda a, b: a // b if b != 0 else None)  # integer division
}

def question_generator(count=10, operation="1", filename="questions.txt"):
    """Generate math questions and save them to a file."""
    numbers = list(range(1, 10))  # avoid zero for division
    symbol, func = OPERATIONS[operation]

    with open(filename, "w") as f:
        for i in range(1, 11):
            num1 = random.choice(numbers)
            num2 = random.choice(numbers)
            if symbol == "/" and num2 == 0:  # avoid divide by zero
                num2 = random.choice(numbers[1:])
            question = f"{i}. {num1} {symbol} {num2} = ___"
            print(question)
            f.write(question + "\n")

def main():
    while True:
        print("*" * 50)
        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("What do you want to do? ")

        if choice in OPERATIONS:
            question_generator(count=10, operation=choice)
            print("Questions saved to questions.txt")
        elif choice == "5":
            print("Thanks for using this program! We hope your math knowledge improved.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()