from tkinter import *
from tkinter import messagebox
from game_folder.game import run_game

def main():
#################APP SETUP
    app = Tk()
    app.geometry('500x500')
    app.title('Chase')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")
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

    def exit_game_funtion():
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()

    def leaderboard_function():
            app.destroy()
            run_board()

##################BUTTONS AND LABELS
    empty = Label(app,text='',background='black')
    empty.pack()

    name = Label(app,text='CHASE',background='black',font=('Palatino',8),fg='white')
    name.pack()

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,40))

    play = Button(app,text='Play',command=play_game,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    play.pack(pady=padding)

    play_hard = Button(app,text='Play HardMode',command=play_hard_mode,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    play_hard.pack(pady=padding)

    leaderboard = Button(app,text='View Leaderboard',command=leaderboard_function,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    leaderboard.pack(pady=padding)

    exit_game = Button(app,text='Exit',command=exit_game_funtion,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    exit_game.pack(pady=padding)

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,80))

    year = Label(app, text='2024',font=('Palatino',8),fg='white',background='black')
    year.pack()

    mainloop()


def run_board():
#################APP SETUP
    app = Tk()
    app.geometry('500x500')
    app.title('Leaderboard')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")
    padding = (5,5)


    def back_to_home():
        app.destroy()
        main()


    def exit_game_function():
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()


    empty = Label(app,text='',background='black')
    empty.grid(row=1)

    name = Label(app,text='Leaderboard',background='black',font=('Palatino',8),fg='white')
    name.grid(row=2,column=0, columnspan=2)

    empty = Label(app,text='',background='black')
    empty.grid(row=3)

    # board = Listbox(app,highlightcolor='red')
    # board.grid(row=4,column=0, sticky='nsew',columnspan=2)

    # leaderboard = Button(app,text='Back to Home',command=back_to_home,font=('Palatino',8),highlightbackground='red')
    # leaderboard.grid(row=5,column=0)

    # exit_game = Button(app,text='Exit',command=exit_game_function,font=('Palatino',8),highlightbackground='red')
    # exit_game.grid(row=5,column=1)

    app.grid_rowconfigure(4, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    board = Listbox(app, highlightcolor='red')
    board.grid(row=4, column=0, sticky='nsew', columnspan=2)


    leaderboard_data = [
        ("Player 1", 100),
        ("Player 2", 80),
        ("Player 3", 120)
    ]

    board = Listbox(app, highlightcolor='red', font=('Palatino', 8))
    board.grid(row=4, column=0, sticky='nsew', columnspan=2)

    # Insert data into the listbox in a table-like format
    for name, score in leaderboard_data:
        board.insert('end', f"{name:<20}{score:>10}")



    leaderboard = Button(app, text='Back to Home', command=back_to_home, font=('Palatino',8), highlightbackground='red')
    leaderboard.grid(row=5, column=0, sticky='ew')

    exit_game = Button(app, text='Exit', command=exit_game_function, font=('Palatino',8), highlightbackground='red')
    exit_game.grid(row=5, column=1, sticky='ew')


    mainloop()

run_board()


# if __name__ == '__main__':
#     main()