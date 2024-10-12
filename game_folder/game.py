import random
from turtle import *
from tkinter import messagebox
from music import BackgroundMusic
from databases import update_score
import sqlite3


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


######################KEYBOARD AND DIRECTIONS
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

def random_target() -> tuple:
    """_Generates random coordinates_

    Returns:
        _tuple_: _random coordinayes_
    """

    return (random.randint(-295,295),random.randint(-295,295))


######################BORDER
def the_border():
    """_Creates a border on game screen_
    """

    border = Border()
    border.setpos(-300,300)

    for i in range(4):
        border.pendown()
        border.forward(600)
        border.right(90)

def game_zone_check(item) -> bool:
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


def add_to_db(name, score, mode):
    """_Adds a player's score to the database for the specified game mode._

    Parameters:
    name (_str_): The name of the player.
    score (_int_): The score achieved by the player.
    mode (_bool_): The game mode; True for hard mode, False for normal mode.

    If the name or score is empty, the function will skip the database update.
    """
    if not name or not score:
        print("Name or score is missing. Skipping database update.")
        return

    with sqlite3.connect('scoreboard.db') as connection:
        cursor = connection.cursor()

        update_score(cursor, name, score, mode)
        connection.commit()


########################HANDLING SOUND
def game_over_sound():
    """_stops game music and play game over sound_
    """
    BackgroundMusic.stop_background_music()
    BackgroundMusic.play_background_music("background_music/game-over-38511.mp3")

def random_play() -> str:
    """_Select a random music file from a predefined list and return its path.
    
    This function randomly selects a music file from a list of predefined
    music file names and returns the file path as a string._

    Returns:
        str: _The file path of the randomly selected music file._
    """
    music = ["arcade-party-173553.mp3", "big-jason-slap-house-version-background-music-for-video-vlog-1minute-223905.mp3","flow-211881.mp3"]
    play_sound = random.randint(0, len(music) - 1)
    return f"background_music/{music[play_sound]}"


def run_game(hard_mode = False):
    BackgroundMusic.stop_background_music()
    BackgroundMusic.play_background_music(random_play())

###################SETUP WINDOW
    window = Screen()
    window.title("Chase")
    window.bgcolor('black')
    window.setup(800,800)

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
            game_over_sound()
            messagebox.showwarning("Alert", f"Game Over\n \nYour Score: {score}")
            get_name = window.textinput('Name', 'Enter your name:')
            add_to_db(get_name,score,hard_mode)
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
                game_over_sound()
                messagebox.showwarning("Alert", f"Game Over\n \nYour Score: {score}")
                get_name = window.textinput('Name', 'Enter your name:')
                add_to_db(get_name,score,hard_mode)
                window.bye()
            
        window.update()
