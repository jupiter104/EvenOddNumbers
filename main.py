# This program lists odd or even numbers within
# a range given by the user.
# Author: Debashis B. Jupiter

numbering = 0
choice_full = ""

choice = input("Even or odd numbers? Type e or o: ")
lower_range = int(input("Enter starting number: "))
upper_range = int(input("Enter ending number: "))

if choice == 'e':
    choice_full = "even"
    for number in range(lower_range, upper_range + 1):
        if number % 2 == 0:
            numbering += 1
            print(f"{numbering}. {number}")
elif choice == 'o':
    choice_full = "odd"
    for number in range(lower_range, upper_range + 1):
        if number % 2 == 1:
            numbering += 1
            print(f"{numbering}. {number}")
else:
    print("Invalid choice.")

print(f"There are {numbering} {choice_full} numbers." )
