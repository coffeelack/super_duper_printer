#!python3
"""
This program prints a given word letter by letter with a given list of characters.
It can be used to test the performance of different lists of characters.
"""

# Imports
from time import sleep, perf_counter
import os

# Variables
SENTENCE = 'This is an example of a \'Hello World\' programm.'  # Sentence to print, watch for right quotation marks
TRIES = 0  # Counts the number of loops it takes to print the sentence
SLEEP_TIME = 0.02  # Time between each loop, set to 0.02 for best visibility in console
# List of characters to print the sentence with
ENI = [" ", ",", ".", "e", "n", "i", "s", "r", "t", "u",
       "a", "h", "d", "l", "c", "g", "m", "o", "b", "w",
       "f", "k", "z", "v", "p", "j", "y", "x", "q", "ä",
       "ö", "ü", "E", "N", "I", "S", "R", "T", "U", "A",
       "H", "D", "L", "C", "G", "M", "O", "B", "W", "F",
       "K", "Z", "V", "P", "J", "Y", "X", "Q", "ß", "Ä",
       "Ö", "Ü", "1", "2", "3", "4", "5", "6", "7", "8",
       "9", "0", "?", "!", "@", "#", "$", "%", "&", "*",
       "(", ")", "-", "_", "+", "=", "[", "]", "{", "}",
       "|", "\\", "/", "<", ">", ";", ":", "'", '"']


# Functions
def super_duper_printer(words='Hello World!', char_list=None, tries=0):
    """
    Prints a given word letter by letter with a given list of characters.
    :param words: Word to print, default is 'Hello World!', watch for right quotation marks
    :param char_list: List of characters to print the sentence with, default is None
    :param tries: Counts the number of loops it takes to print the sentence, default is 0
    :return: Runtime of the loop and number of tries it took to print the sentence
    """
    if char_list is None:
        char_list = ['H', 'e', 'l', 'o', 'W', 'r', 'd', '!']
    # Start timer for performance test
    start = perf_counter()
    # Split word into list of chars
    words_list = list(words)
    previous = ""
    # Loop through chars in words_list
    for char in words_list:
        # Loop through chars in char_list to find matching char
        for i in char_list:
            # Clear console and print the previous chars plus the current try from char_list
            os.system('cls')
            print(previous + i)
            tries += 1
            sleep(SLEEP_TIME)
            # If char is found, add it to previous and break loop
            if char == i:
                previous = previous + char
                break

    # Stop timer for performance test
    stop = perf_counter()
    loop_runtime = stop - start
    return loop_runtime, tries


# Main
if __name__ == '__main__':
    RUNTIME, TRIES = super_duper_printer(SENTENCE, ENI, TRIES)
    print(f"\nRuntime: {RUNTIME:0.4f} seconds")
    print(f"Tries: {TRIES}")
