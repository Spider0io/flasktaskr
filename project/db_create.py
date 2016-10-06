#project/db_create.py
import sqlite3
from _config import DATABASE_PATH
with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE task(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              due_date TEXT NOT NULL,
              priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

    # insert dumy data into the table
    c.execute(
        'INSERT INTO task (name, due_date, priority, status)'
        'VALUES("FINISH this tutorial", "03/25/2015", 10, 1)'
    )
    c.execute(
        'INSERT INTO task (name, due_date, prioritu, status)'
        'VALUES("Finish Real Python COurse 2", "03/25/2015", 10, 1)'
    )
