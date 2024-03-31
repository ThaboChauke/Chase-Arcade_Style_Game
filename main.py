from turtle import *
import random
from tkinter import messagebox


###################SETUP WINDOW
window = Screen()
window.title("Chase-Snake_Type")
window.bgcolor('black')
window.setup(700,700)


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


############TURTLE CALLS
chaser = Chaser()
score_keeper = Score_Keeper()
target = Target()
################KEYBOARD AND DIRECTIONS

def Turn_left():
    chaser.left(30)

def Turn_right():
    chaser.right(30)

def keyboard():
    listen()
    onkey(Turn_left, 'Left')
    onkey(Turn_right, 'Right')


################TARGETS AND BORDER
def random_target():
    target = (random.randint(-295,295),random.randint(-295,295))
    return target

def the_border():
    border = Border()
    border.setpos(-300,300)

    for i in range(4):
        border.pendown()
        border.forward(600)
        border.right(90)


def game_zone_check(item):
    return item.xcor() <= -300 or item.xcor() >=  300 or item.ycor() <= -300 or item.ycor() >= 300


def keeping_score(item,score):
    item.undo()
    item.setposition(-290,310)
    current_score = f"Score: {score}"
    item.write(current_score,False,align='left',font=('Arial',14,'normal'))


def run_game():
    the_border()
    keyboard()
    target_coords = random_target()

    target.goto(target_coords)
    target.stamp()

    score = 0

    while True:
        chaser.forward(5)
        chaser.speed(3)
        
        if game_zone_check(chaser):
            chaser.right(180)
            messagebox.showwarning("Alert", f"Game Over\n \nYour Score: {score}")
            get_name = window.textinput('Name', 'Enter your name:')
            window.bye()

        elif chaser.distance(target) < 20:
            target.clearstamps()
            target_coords = random_target()
            target.goto(target_coords)
            target.stamp()
            score += 1
            keeping_score(score_keeper,score)
            
        window.update()


if __name__ == '__main__':
    run_game()
    