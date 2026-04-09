import random
import string
import time

def generate_password(length):
    if length < 4:
        print("Password must be at least 4 characters long.")
        return None

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!%"

    all_categories = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_symbols = lower + upper + digits + symbols
    all_categories += random.choices(all_symbols, k=length - 4)

    random.shuffle(all_categories)

    return ''.join(all_categories)

def main():
    while True:
        start = input("Do you want to generate a password? (yes/no): ").strip().lower()
        if start == "no":
            print("The program is complete. Thank you for using it! Have a nice day!")
            time.sleep(10)
            break
        elif start == "yes":
            while True:
                try:
                    length = int(input("Enter length of password: "))
                    password = generate_password(length)
                    if password:
                        print(f"Your random password: {password}")

                        repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
                        if repeat == 'no':
                            print("The program is complete. Thank you for using it! Have a nice day!")
                            time.sleep(10)
                            return
                        elif repeat == 'yes':
                            continue
                        else:
                            print("Please enter 'yes' or 'no'.")
                            continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
