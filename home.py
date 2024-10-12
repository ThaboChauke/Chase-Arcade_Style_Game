import sqlite3
from tkinter import *
from databases import view
from tkinter.ttk import Combobox
from music import BackgroundMusic
from game_folder.game import run_game
from tkinter import messagebox, StringVar


def menu_music():
    BackgroundMusic.play_background_music("background_music/save-as-115826.mp3")

menu_music()

def main():
#################APP SETUP
    app = Tk()
    app.geometry('800x800')
    app.title('Chase')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")
    padding = (5,5)


###################COMMANDS
    def play_game():
        try:
            app.destroy()
            run_game()
        except :
            menu_music()
            main()       

    def play_hard_mode():
        try:
            app.destroy()
            run_game(True)
        except :
            menu_music()
            main()        

    def exit_game_funtion():
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()

    def leaderboard_function():
            app.destroy()
            run_board()

    def help_function():
        app.destroy()
        run_help()

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

    game_help = Button(app,text='Help',command=help_function,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    game_help.pack(pady=padding)

    exit_game = Button(app,text='Exit',command=exit_game_funtion,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    exit_game.pack(pady=padding)

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,80))

    year = Label(app, text='2024',font=('Palatino',8),fg='white',background='black')
    year.pack()

    mainloop()

def run_help():
#################APP SETUP
    app = Tk()
    app.geometry('800x800')
    app.title('Chase - Help')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")

    def back_to_home():
        app.destroy()
        main()

    def exit_game_function():
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()


    empty = Label(app,text='',background='black')
    empty.grid(row=1)

    name = Label(app,text='Chase - Help',background='black',font=('Palatino',16),fg='white')
    name.grid(row=2,column=0, columnspan=2)

    empty = Label(app,text='',background='black')
    empty.grid(row=3)

    
    app.grid_rowconfigure(4, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    help_text = Text(app, wrap=WORD, font=('Palatino', 12), bg='black', fg='white', bd=0, highlightthickness=0)
    help_text.grid(row=4, column=0, sticky='nsew', columnspan=2)

    help_content = """
    Welcome to "Chase" Help!

    In this game, your objective is to move around and hit
    target, as many as you can.

    Controls:
    - Use the left and right arrow keys to move your character.

    Game Modes:
    - Play: Start a regular game session.
    - Play HardMode: Engage in a more challenging game experience.

    Leaderboard:
    - View Leaderboard: See top scores of other players.

    Exiting the Game:
    - Use the 'Exit' button to close the game.

    Enjoy playing "Chase"!

    """

    help_text.insert(END, help_content)

    leaderboard = Button(app, text='Back to Home', command=back_to_home, font=('Palatino',8), highlightbackground='red')
    leaderboard.grid(row=5, column=0, sticky='ew')

    exit_game = Button(app, text='Exit', command=exit_game_function, font=('Palatino',8), highlightbackground='red')
    exit_game.grid(row=5, column=1, sticky='ew')

    mainloop()

def run_board():
#################APP SETUP
    app = Tk()
    app.geometry('800x800')
    app.title('Chase - Leaderboard')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")

    def back_to_home():
        app.destroy()
        main()

    def exit_game_function():
        prompt = messagebox.askyesno('Exit', 'Are you sure?')
        if prompt:
            app.destroy()

    def update_leaderboard(mode):
        """Update the Listbox to show the leaderboard for the selected mode."""
        board.delete(0, 'end')

        with sqlite3.connect('scoreboard.db') as connection:
            cursor = connection.cursor()
            leaderboard_data = view(cursor, mode)

        for name, score in leaderboard_data:
            board.insert('end', f"{name:<20}{score:>10}")

    empty = Label(app,text='',background='black')
    empty.grid(row=1)

    name = Label(app,text='Leaderboard',background='black',font=('Palatino',16),fg='white')
    name.grid(row=2,column=0, columnspan=2)

    empty = Label(app,text='',background='black')
    empty.grid(row=3)

    app.grid_rowconfigure(4, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    board = Listbox(app, highlightcolor='red', font=('Palatino', 12))
    board.grid(row=4, column=0, sticky='nsew', columnspan=2)

    mode_var = StringVar()
    mode_combobox = Combobox(app, textvariable=mode_var, values=['normal', 'hard'], state='readonly')
    mode_combobox.grid(row=3, column=0, columnspan=2)
    mode_combobox.current(0) 

    def on_mode_change(event):
        selected_mode = mode_var.get()
        update_leaderboard(selected_mode)

    mode_combobox.bind("<<ComboboxSelected>>", on_mode_change)

    update_leaderboard(mode_combobox.get())

    leaderboard = Button(app, text='Back to Home', command=back_to_home, font=('Palatino',8), highlightbackground='red')
    leaderboard.grid(row=5, column=0, sticky='ew')

    exit_game = Button(app, text='Exit', command=exit_game_function, font=('Palatino',8), highlightbackground='red')
    exit_game.grid(row=5, column=1, sticky='ew')

    mainloop()

if __name__ == '__main__':
    main()
    