import pandas as pd
from termcolor import colored
from colorama import init
import os

init()

#This reads in the pandas data and places the values into a dictionary to be read later. 
new_dataframe = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')
new_dictionary = dict(zip(new_dataframe['letter'], new_dataframe['code']))

def clearingline():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 

clearingline()
main_loop = True
while main_loop:
    print(' ') #this is in place to create a fresh line for the below input prompt.
    user_input = input('Please input your word: ')
    try:
        word_split = [*user_input.lower()]
        returning_words = []
        for letter in word_split:
            returning_words.append(new_dictionary[letter.upper()])
        for word in returning_words:
            print(colored(word + '            ', color="green", attrs=["bold"]), end=" ")
    except:
        print('Please enter a single word with no numbers or spaces')
    
