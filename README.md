# PandasProjects

#### This is a collection of projects that utilise Python Pandas library. 
![Pandas](https://geo-python.github.io/site/_images/pandas_logo.png)

# State guessing game
### This is a game that uses the Turtle library and Pandas library in order to create an educational game in which the user attempts to guess the states in the US. The game functions in this order;
#### -The screen is drawn using the Turtle class
#### -The map of the US is drawn using an image
#### -Using Pandas the data is extracted from the CSV file which contains all states and coordinates. 
#### -The states are added to a list in order to be edited.
#### -The coordinates are added to a dictionary. 
#### -As the user is prompted to make a guess, the guess is checked against the library and if it matches an unpicked state, an object will draw the states name on the map.
#### -The picked state is then removed from the list. 
#### -If all states are selected the game issues a winning message. If the user types exit, a new CSV file is created containing all the states the use failed to remember. 
![Pandas game](https://github.com/PureJD/PandasProjects/blob/main/country_guessing_game/game_image.png?raw=true)
# NATO Alphabet assistant
### This is an assistant that will input a word and provide you with the Nato alphabet words. The program runs;
#### -The inital data is read from a csv using Pandas and formatted into a dictionary. 
#### -The program then takes an input from the user and splits the word into a new dictionary of the idividual letters.
#### -These letters are matched to the words in the dictionary and the words are returned in a formatted style for ease of reading. 
![Pandas game2](https://github.com/PureJD/PandasProjects/blob/main/project_images/nato.png?raw=true)













