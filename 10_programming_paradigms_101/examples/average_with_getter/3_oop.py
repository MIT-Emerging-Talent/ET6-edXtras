#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===== define class =====

class Averager():
    # data is hard coded -> _ -> data is saved to instance properties
    def __init__(self):
        # hard coded data -> _ -> instance property
        self.user_numbers = []

    # from args & input -> gathers & validates input -> saved to instance property
    def gather_numbers(self, prompt: str = 'enter a number or "done"'):
        while True:
            # argument data -> printed to CLI -> _
            # CLI input -> _ -> save to local variable
            user_input = input(prompt)

            # read local variable -> use for comparison -> _
            if user_input == "" or user_input is None:
                print("nothing is not allowed")
                continue

            # read local variable -> use for comparison -> _
            if user_input.lower() == "done":
                break

            try:
                # local variable -> cast to float -> new local variable 
                next_number = float(user_input)
                # local variable -> _ -> instance property's list
                self.user_numbers.append(next_number)
            except ValueError:
                # local variable -> print to CLI -> _
                print(f'"{user_input}" is not a number, it has been ignored')

    # data from instance properties -> calculates average of state -> returns average
    def get_average(self):
        if len(self.user_numbers) == 0:
            return 0
        else:
            return sum(self.user_numbers) / len(self.user_numbers)

    # data is from args & hard coding -> proceseed by methods-> printed to the CLI
    def main(self, name: str=''):
        # argument data -> used in conditional -> _
        if name:
            # argument data -> printed to CLI -> _
            print("\n", name, "\n\n")

        print(
        "\ncalculate the average of many numbers:\n\n"
        "- you must input something\n"
        "- input a number and it will be added to the sum\n"
        '- input "done" and the program will finish (case insensitive)\n'
        "- input anything else and it will be ignored\n\n"
        "when you have finished inputting numbers, the average will be displayed\n\n"
        )

        # calling method that update instance state
        self.gather_numbers("enter a number to add, or 'done' to finish\n>>> ")

        # calling method that calculates and returns the average of current state
        average = self.get_average()

        # instance properties -> print to CLI -> _
        print("your numbers are: ", self.user_numbers)
        print("their average is: ", average)


# ===== use the class =====

# -> entry point
average_program_1 = Averager()
average_program_2 = Averager()

# if you input the same numbers both times, will you get the same average?
average_program_1.main('---- program 1, first run ----')
average_program_2.main('---- program 2, first run ----')

# if you input the same numbers as before, will you get the same averages?
average_program_1.main('---- program 1, second run ----')
average_program_2.main('---- program 2, second run ----')
