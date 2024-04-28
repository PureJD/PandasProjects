import turtle
import pandas
from turtle import Turtle
import time 

IMAGE = 'blank_states_img.gif'
screen = turtle.Screen()
screen.setup(width= 725, height= 491)
screen.title('U.S. States Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Amount of answers correct. Game will end when hits 50
amount_of_correct_answers = 0

country_data = pandas.read_csv('50_states.csv')
countries_list = list(country_data['state'])
country_locations_dictionary = {state: [x, y] for state, x, y in zip(country_data['state'], country_data['x'], country_data['y'])}

class Country(Turtle): 
    '''The class object for creating the names on screen. Super class'''
    def __init__(self):
        super().__init__()
        self.color('Black')
        self.penup()
        self.hideturtle()


    def draw_countries(self, x, y, country_name):
        '''The function to draw the objects to screen'''
        self.goto(x, y)
        self.write( arg= (f'{country_name}') , move= False, align= 'center', font= ('courier', 8, 'normal'))

    def winner_message(self):
        self.goto(0, 0)
        self.write( arg= ('Congratulations! you have named all 50 states!') , move= False, align= 'center', font= ('courier', 8, 'normal'))


country1 = Country() #Initiation of the class

loop = True
while loop:
    answer_state = screen.textinput(title=f'Guess the State {amount_of_correct_answers}/50', prompt='What\'s another state?')
    if answer_state.title() in countries_list:
        amount_of_correct_answers += 1
        countries_list.remove(answer_state.title())
        country1.draw_countries(country_locations_dictionary[answer_state.title()][0], country_locations_dictionary[answer_state.title()][1], answer_state.title())

    if amount_of_correct_answers == 50:
        country1.winner_message()
        time.sleep(2)
        loop = False
        break 
    
    if answer_state.title() == 'Exit':
        left_overs = pandas.DataFrame(countries_list)
        left_overs.to_csv('countries_missed.csv')
        loop = False
        break 
    
    screen.exitonclick