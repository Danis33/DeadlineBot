import sqlite3


def init_db():
    conn = sqlite3.connect("database/bot.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS task(
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        task_text TEXT NOT NULL
        )''')

    conn.commit()
    conn.close()


def add_task(user_id, task_text):
    conn = sqlite3.connect("database/bot.db")
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO task(user_id, task_text) VALUE(?, ?)''', (user_id, task_text))
    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = sqlite3.connect("database/bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task_text FROM task WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
