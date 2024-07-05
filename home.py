import json
from tkinter import *
from tkinter import messagebox
from game_folder.game import run_game
from music import BackgroundMusic


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
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()


    empty = Label(app,text='',background='black')
    empty.grid(row=1)

    name = Label(app,text='Leaderboard',background='black',font=('Palatino',16),fg='white')
    name.grid(row=2,column=0, columnspan=2)

    empty = Label(app,text='',background='black')
    empty.grid(row=3)


    app.grid_rowconfigure(4, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    board = Listbox(app, highlightcolor='red')
    board.grid(row=4, column=0, sticky='nsew', columnspan=2)

    leaderboard_data = read_leaderboard_from_json()

    board = Listbox(app, highlightcolor='red', font=('Palatino', 12))
    board.grid(row=4, column=0, sticky='nsew', columnspan=2)

    for name, score in leaderboard_data:
        board.insert('end', f"{name:<20}{score:>10}")

    leaderboard = Button(app, text='Back to Home', command=back_to_home, font=('Palatino',8), highlightbackground='red')
    leaderboard.grid(row=5, column=0, sticky='ew')

    exit_game = Button(app, text='Exit', command=exit_game_function, font=('Palatino',8), highlightbackground='red')
    exit_game.grid(row=5, column=1, sticky='ew')

    mainloop()


def read_leaderboard_from_json():
    """_Reads player's data from json file_

    Returns:
        _list_: _list of tuples containing names and scores of players_
    """
    
    try:
        with open('leaderboard.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    leaderboard_data = []
    for entry in data:
        for name, score in entry.items():
            leaderboard_data.append((name, int(score)))

    return leaderboard_data


if __name__ == '__main__':
    main()