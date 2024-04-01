import os
from tkinter import *
from tkinter import messagebox
from game_folder.game import run_game

def main():
#################APP SETUP
    app = Tk()
    app.geometry('500x500')
    app.title('Chase')
    app.config(background='black')
    padding = (5,5)

###################COMMANDS
    def play_game():
        try:
            app.destroy()
            run_game()
        except :
            app.mainloop()        

    def play_hard_mode():
        try:
            app.destroy()
            run_game(True)
        except :
            main()        

    def exitGame():
        os.system('clear')
        app.quit()


##################BUTTONS AND LABELS
    empty = Label(app,text='',background='black')
    empty.pack()

    name = Label(app,text='CHASE',background='black',font=('Palatino',8),fg='white')
    name.pack()

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,40))

    play = Button(app,text='Play',command=play_game,width=20,height=2,highlightbackground='red')
    play.pack(pady=padding)

    play_hard = Button(app,text='Play Hardmode',command=play_hard_mode,width=20,height=2,highlightbackground='red')
    play_hard.pack(pady=padding)

    leaderboard = Button(app,text='View Leaderboard',command='',width=20,height=2,highlightbackground='red')
    leaderboard.pack(pady=padding)

    exit_game = Button(app,text='Exit',command=exitGame,width=20,height=2,highlightbackground='red')
    exit_game.pack(pady=padding)

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,80))

    year = Label(app, text='2024',font=('Palatino',8),fg='white',background='black')
    year.pack()


    mainloop()


if __name__ == '__main__':
    main()