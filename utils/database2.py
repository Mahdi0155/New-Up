import sqlite3

conn = sqlite3.connect('bot.db')
cur = conn.cursor()

def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS admins (
        user_id INTEGER PRIMARY KEY
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id TEXT,
        caption TEXT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT
    )""")
    conn.commit()

def add_admin(user_id):
    cur.execute("INSERT OR IGNORE INTO admins (user_id) VALUES (?)", (user_id,))
    conn.commit()

def remove_admin(user_id):
    cur.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
    conn.commit()

def get_admins():
    cur.execute("SELECT user_id FROM admins")
    return [row[0] for row in cur.fetchall()]

def save_file(file_id, caption):
    cur.execute("INSERT INTO files (file_id, caption) VALUES (?, ?)", (file_id, caption))
    conn.commit()

def get_file_by_index(index):
    cur.execute("SELECT id, file_id, caption FROM files ORDER BY id ASC")
    files = cur.fetchall()
    if 0 <= index < len(files):
        return files[index]
    return None

def delete_file_by_id(file_id):
    cur.execute("DELETE FROM files WHERE id=?", (file_id,))
    conn.commit()

def add_channel(channel_id):
    cur.execute("INSERT INTO channels (channel_id) VALUES (?)", (channel_id,))
    conn.commit()

def remove_channel(channel_id):
    cur.execute("DELETE FROM channels WHERE channel_id=?", (channel_id,))
    conn.commit()

def get_channels():
    cur.execute("SELECT channel_id FROM channels")
    return [row[0] for row in cur.fetchall()]
