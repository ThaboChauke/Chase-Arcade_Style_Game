import sqlite3


def create_tables(cursor):
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
    if mode == "normal":
        mode_query = "normal_mode"
    elif mode == "hard":
        mode_query = "hard_mode"
    
    cursor.execute(f"SELECT * FROM {mode_query} LIMIT 10")
    return cursor.fetchall()
  
    
def update_score(cursor, name, score, mode):
    if mode == "normal":
        table = "normal_mode"
    elif mode == "hard":
        table = "hard_mode"

    cursor.execute(f"SELECT * FROM {table} WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        cursor.execute(f"UPDATE {table} SET score = ? WHERE name = ?", (score, name))
    else:
        cursor.execute(f"INSERT INTO {table} (name, score) VALUES (?, ?)", (name, score))



def main():
    with sqlite3.connect('scoreboard.db') as connection:
        cursor = connection.cursor()
        create_tables(cursor)
        connection.commit()



if __name__ == '__main__':
    main()