import sqlite3

def create_tables(cursor):
    """
    Creates the tables for the normal and hard game modes if they do not exist.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor object used to execute SQL commands.
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS normal_mode (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hard_mode (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)

def view(cursor, mode):
    """
    Retrieves the top 10 scores from the specified game mode.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor object used to execute SQL commands.
    mode (str): The game mode to retrieve scores from ('normal' or 'hard').

    Returns:
    list: A list of tuples containing the top 10 scores in the specified mode.
    """
    if mode == "normal":
        mode_query = "normal_mode"
    elif mode == "hard":
        mode_query = "hard_mode"
    
    cursor.execute(f"SELECT * FROM {mode_query} LIMIT 10")
    return cursor.fetchall()

def update_score(cursor, name, score, mode):
    """
    Updates the player's score in the specified game mode or inserts a new record
    if the player does not exist.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor object used to execute SQL commands.
    name (str): The name of the player whose score is being updated.
    score (int): The new score for the player.
    mode (bool): The game mode; True for hard mode, False for normal mode.
    """
    table = "hard_mode" if mode else "normal_mode"

    cursor.execute(f"SELECT * FROM {table} WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        cursor.execute(f"UPDATE {table} SET score = ? WHERE name = ?", (score, name))
    else:
        cursor.execute(f"INSERT INTO {table} (name, score) VALUES (?, ?)", (name, score))

def main():
    """
    Main function to create database tables and initialize the SQLite connection.
    """
    with sqlite3.connect('scoreboard.db') as connection:
        cursor = connection.cursor()
        create_tables(cursor)
        connection.commit()

if __name__ == '__main__':
    main()
