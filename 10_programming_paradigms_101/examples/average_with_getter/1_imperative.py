#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -> entry point

print(
    "\ncalculate the average of many numbers:\n\n"
    "- you must input something\n"
    "- input a number and it will be added to the sum\n"
    '- input "done" and the program will finish (case insensitive)\n'
    "- input anything else and it will be ignored\n\n"
    "when you have finished inputting numbers, the average will be displayed\n\n"
)

# ===== initialize program data =====

# --- creating initial data ---
# 1. this logic is not encapsulated
# 2. the data comes from hard-coded values
# 3. the data is saved to global variables

# hard-coded data -> _ -> stored in global variables
numbers = []

# ===== operate on program data =====

# --- gathering user input ---
# 1. the I/O loop is not encapsulated
# 2. it's data comes from global variables and user input
# 3. the resulting data is saved in global variables

while True:
    # CLI input -> _ -> global variable
    user_input = input("enter a number to add, or 'done' to finish\n>>> ")

    # from global variable -> used for comparison -> _
    if user_input == "" or user_input is None:
        print("nothing is not allowed")
        continue

    # from global variable -> use for comparison -> _
    if user_input.lower() == "done":
        break

    try:
        # global variable -> cast input to a float -> another global variable
        next_number = float(user_input)
        # global variable -> _ -> a list in a global variable
        numbers.append(next_number)
    except ValueError:
        # global variable -> print to the console -> _
        print(f'"{user_input}" is not a number, it has been ignored')


# --- averaging the numbers ---
# 1. the computation is not encapsulated
# 2. it's data comes from global variables
# 3. the result is saved in a global variable


#  global variable list -> calculate the average -> save to another global variable
average = sum(numbers) / len(numbers) if len(numbers) > 0 else 0


# --- displaying the results ---
# 1. the logic is not encapsulated
# 2. the data comes from global variables
# 3. these instructions do not generate any data

# global variables -> print to console -> _
print("your numbers are: ", numbers)
print("their average is: ", str(average))

# discussion question: how could you run this program again, or use it in a different file?
