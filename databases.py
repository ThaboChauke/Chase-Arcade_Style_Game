import sqlite3


def create_table(cursor):
    cursor.execute("""
CREATE TABLE IF NOT EXISTS normal_mode (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)
""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS hard_mode (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)
""")
    
def update_score():
    pass
    


def main():
    connection = sqlite3.connect('scoreboard.db')
    cursor = connection.cursor()

    create_table(cursor)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()