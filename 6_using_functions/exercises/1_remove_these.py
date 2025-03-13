#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Program for removing user-specified characters from text.

This program prompts users to enter text and specify characters to remove,
then displays the result using the remove_characters function.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/
"""
from utils.remove_characters import remove_characters


print('Enter some text, then decide what you want to remove from it')

# Get text to modify
original = input('Enter the text to modify: ').strip()
while not original:
    original = input('Please enter some text to modify: ').strip()

# Get characters to remove
remove_these = input(
    f'Enter all the characters you would like to remove from:\n- "{original}"\n'
).strip()
while not isinstance(remove_these, str):  # Type check for defensive programming
    remove_these = input('Please enter the characters to remove: ').strip()

# Use remove_characters to create a new value assigned to removified
removified = remove_characters(original,remove_these)

# Display results
print(f'\nBefore: {original}\nAfter: {removified}')
