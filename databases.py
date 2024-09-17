import sqlite3


def create_table(connection, cursor):
    pass


def main():
    connection = sqlite3.connect('scoreboard.db')
    cursor = connection.cursor()


if __name__ == '__main__':
    main()