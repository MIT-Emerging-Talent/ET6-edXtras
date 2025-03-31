#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- tracing data flow ---
# 1. the first call to `main` is the entry point
# 2. CLI input -> gather_numbers -> main -> average -> main -> CLI
# 3. the logic is encapsulated in procedures, the data is not encapsulated

# ===== declare functions =====
#   quiz: which function is a pure function?  Which one is easier to test?

# data comes from arguments & user input -> data is sent to outer scope
def gather_numbers(prompt: str = 'enter a number or "done"') -> list[float]:
    # hard coded data -> _ -> local variable
    numbers = []

    while True:
        # argument data -> printed to CLI -> _
        # CLI input -> _ -> local variable 
        user_input = input(prompt)

        # local variable -> comparison -> _
        if user_input == "" or user_input is None:
            print("nothing is not allowed")
            continue

        # local variable -> comparison -> _
        if user_input.lower() == "done":
            break

        try:
            # local variable -> cast to float -> different local variable
            next_number = float(user_input)
            # local variable -> _ -> local variable's list
            numbers.append(next_number)
        except ValueError:
            # local variable -> print to CLI -> _
            print(f'"{user_input}" is not a number, it has been ignored')

    # local variable -> _ -> send to global scope
    return numbers


# data comes from arguments -> data is sent to outer scope
def calculate_average(to_average: list[int | float]) -> float:
    # argument data -> calculate average -> send to global scope
    return sum(to_average) / len(to_average) if len(to_average) > 0 else 0


# data comes from arguments & other procedures -> data is printed to CLI
def main(name: str = "") -> None:
    # argument data -> conditional check -> _
    if name:
        # argument data -> printed -> _
        print("\n", name, "\n\n")

    print(
        "\ncalculate the average of many numbers:\n\n"
        "- you must input something\n"
        "- input a number and it will be added to the sum\n"
        '- input "done" and the program will finish (case insensitive)\n'
        "- input anything else and it will be ignored\n\n"
        "when you have finished inputting numbers, the average will be displayed\n\n"
    )

    # return value from gathering procedure -> _ -> save to local variable
    user_numbers = gather_numbers("enter a number to add, or 'done' to finish\n>>> ")

    # data from local variable -> calculate average -> save to local variable
    average = calculate_average(user_numbers)

    # read local variables -> print to CLI -> _
    print("your numbers are: ", user_numbers)
    print("their average is: ", average)


# ===== use functions and data =====
# if you input the same numbers both times, will you get the same average?

# -> entry point
main("--- first time ---")

main("--- second time ---")
