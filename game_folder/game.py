import json
import random
from turtle import *
from tkinter import messagebox


####################SETUP TURTLES
class Chaser(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('arrow')
        self.color('white')
        self.speed(10)
        self.penup()

class Score_Keeper(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed(0)

class Target(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.speed(0)
        self.penup()

class Border(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.hideturtle()
        self.pencolor('blue')
        self.pensize(3)
        self.speed(0)
        self.penup()

class Obstacle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('square')
        self.begin_fill()
        self.color('white','red')
        self.end_fill()
        self.speed(0)
        self.penup()


################KEYBOARD AND DIRECTIONS
def keyboard(item):
    """_Creates keys to control the layer's turtle_

    Args:
        item (_Chaser_): _a Turtle Class_
    """

    def Turn_left():
        item.left(30)

    def Turn_right():
        item.right(30)

    listen()
    onkey(Turn_left, 'Left')
    onkey(Turn_right, 'Right')


def random_target():
    """_Generates random coordinates_

    Returns:
        _tuple_: _random coordinayes_
    """

    return (random.randint(-295,295),random.randint(-295,295))


def the_border():
    """_Creates a border on game screen_
    """

    border = Border()
    border.setpos(-300,300)

    for i in range(4):
        border.pendown()
        border.forward(600)
        border.right(90)


def game_zone_check(item):
    """_Checks if item in gamezone_

    Args:
        item (_Chaser_): _a Turtle Class_

    Returns:
        _bool_: _returns True if outside the gamezone and False otherwise_
    """

    return item.xcor() <= -300 or item.xcor() >=  300 or item.ycor() <= -300 or item.ycor() >= 300


#######################KEEPING TRACK
def keeping_score(item,score):
    """_Writes and updates the player's score on the turtle screen_

    Args:
        item (_Score_Keeper): _a Turtle Class_
        score (_int_): _player's score_
    """

    item.undo()
    item.setposition(-290,310)
    current_score = f"Score: {score}"
    item.write(current_score,False,align='left',font=('Palatino',14,'normal'))


def add_to_json(name,score):
    """_This function adds the user's name to a dictionary with score
    as key and updates json file_
    """

    data_1 = []
    final_data = []

    with open('leaderboard.json', mode='r') as file:
        data_1.append(json.load(file))
    
    tasks_at_end = {name:str(score)}
    for i in data_1:
        if type(i) is list:
            final_data.append(i[1])
        else:
            final_data.append(i)
    final_data.append(tasks_at_end)

    with open('leaderboard.json', mode='w') as f:
        json.dump(final_data,f)

    return

def run_game(hard_mode = False):

###################SETUP WINDOW
    window = Screen()
    window.title("Chase")
    window.bgcolor('black')
    window.setup(700,700)

############TURTLE CALLS
    chaser = Chaser()
    score_keeper = Score_Keeper()
    target = Target()

########################
    the_border()
    keyboard(chaser)
    obstacles = []
    score = 0

############FIRST TARGET
    target_coords = random_target()
    target.goto(target_coords)
    target.stamp()

####################OBSTACLES
    if hard_mode:
        for _ in range(10):
            obstacle = Obstacle()
            obstacle_coords = random_target()
            obstacle.setposition(obstacle_coords)
            obstacle.stamp()
            obstacles.append(obstacle)

    while True:
        chaser.forward(5)
        chaser.speed(3) 

        if game_zone_check(chaser):
            messagebox.showwarning("Alert", f"Game Over\n \nYour Score: {score}")
            get_name = window.textinput('Name', 'Enter your name:')
            add_to_json(get_name,score)
            window.bye()

        elif chaser.distance(target) < 20:
            target.clearstamps()
            target_coords = random_target()
            if target_coords in obstacles:
                target_coords = random_target()
            else:
                target.goto(target_coords)
                target.stamp()
                score += 1
                keeping_score(score_keeper,score)

        for obstacle in obstacles:
            if chaser.distance(obstacle) < 20:
                messagebox.showwarning("Alert", f"Game Over\n \nYour Score: {score}")
                get_name = window.textinput('Name', 'Enter your name:')
                add_to_json(get_name,score)
                window.bye()
            
        window.update()
