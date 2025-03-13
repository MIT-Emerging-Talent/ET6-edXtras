#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for demonstrating string reversal operations.

This program shows how to reverse either entire text or individual words.
Contains code sections marked for refactoring into a separate utility function.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/
"""
from typing import Optional
from utils.reverse_string import reverse_string


def get_validated_input(prompt: str, 
                       error_msg: str = "Please enter something",
                       validator: Optional[callable] = None) -> str:
    """Get and validate user input.

    Args:
        prompt: The message to show when requesting input
        error_msg: Message to show if validation fails
        validator: Optional function to validate input

    Returns:
        str: The validated user input
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_msg)
            continue
        if validator and not validator(user_input):
            print(error_msg)
            continue
        return user_input


def main() -> None:
    """Run the main program loop.
    
    Prompts user for text and reversal preference, then demonstrates
    string reversal with code marked for refactoring.
    """
    print('Enter some text, then decide if you want to reverse the whole thing or each word')
    
    # Get validated input
    original = get_validated_input('Enter the text to reverse: ')
    
    # Get reversal preference
    reverse_words = input(
        'What do you want to reverse?\n'
        '- Enter y for each word, n for whole thing: '
    ).lower().startswith('y')
    
    # Process text based on user choice
    if reverse_words:
        split_text = original.split(' ')
        new_words = []
        for word in split_text:
            # BEGIN: refactor this to call `reverse`
            reversed_word = reverse_string(word)
            # END: refactor
            new_words.append(reversed_word)
        reversed_text = ' '.join(new_words)
    else:
        # BEGIN: refactor this to call `reverse`
        reversed_text = reverse_string(original)
        # END: refactor
    
    print(f'Before: {original}\nAfter: {reversed_text}')


if __name__ == '__main__':
    main()
