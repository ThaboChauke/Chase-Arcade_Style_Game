from tkinter import *
from tkinter import messagebox
# from game_folder.game import run_game


def run_board():
#################APP SETUP
    app = Tk()
    app.geometry('500x500')
    app.title('Leaderboard')
    app.config(background='black',highlightthickness=4,highlightcolor='red',highlightbackground="blue")
    padding = (5,5)


    def back_to_home():
        app.destroy()


    def exit_game_function():
        prompt = messagebox.askyesno('Exit', 'Are you sure')
        
        if prompt:
            app.destroy()


    empty = Label(app,text='',background='black')
    empty.pack()

    name = Label(app,text='Leaderboard',background='black',font=('Palatino',8),fg='white')
    name.pack()

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,40))

    board = Listbox(app,highlightcolor='red')
    board.pack()

    leaderboard = Button(app,text='Back to Home',command=back_to_home,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    leaderboard.pack(pady=padding)

    exit_game = Button(app,text='Exit',command=exit_game_function,width=20,height=2,font=('Palatino',8),highlightbackground='red')
    exit_game.pack(pady=padding)

    empty = Label(app,text='',background='black')
    empty.pack(pady=(0,80))

    year = Label(app, text='2024',font=('Palatino',8),fg='white',background='black')
    year.pack()


    mainloop()

run_board()