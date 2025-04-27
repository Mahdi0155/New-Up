import sqlite3

class Database:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS files (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                file_id TEXT,
                                file_type TEXT,
                                caption TEXT,
                                message_id INTEGER,
                                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                                user_id INTEGER PRIMARY KEY
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS settings (
                                name TEXT PRIMARY KEY,
                                value TEXT
                            )''')
        self.conn.commit()

    def add_file(self, file_id, file_type, caption, message_id):
        self.cursor.execute("INSERT INTO files (file_id, file_type, caption, message_id) VALUES (?, ?, ?, ?)",
                            (file_id, file_type, caption, message_id))
        self.conn.commit()

    def get_file_by_id(self, file_db_id):
        self.cursor.execute("SELECT * FROM files WHERE id=?", (file_db_id,))
        return self.cursor.fetchone()

    def delete_file_by_id(self, file_db_id):
        self.cursor.execute("DELETE FROM files WHERE id=?", (file_db_id,))
        self.conn.commit()

    def add_admin(self, user_id):
        self.cursor.execute("INSERT OR IGNORE INTO admins (user_id) VALUES (?)", (user_id,))
        self.conn.commit()

    def remove_admin(self, user_id):
        self.cursor.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
        self.conn.commit()

    def get_all_admins(self):
        self.cursor.execute("SELECT user_id FROM admins")
        return [row[0] for row in self.cursor.fetchall()]

    def save_setting(self, name, value):
        self.cursor.execute("INSERT OR REPLACE INTO settings (name, value) VALUES (?, ?)", (name, value))
        self.conn.commit()

    def get_setting(self, name):
        self.cursor.execute("SELECT value FROM settings WHERE name=?", (name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_all_files(self):
        self.cursor.execute("SELECT id, caption FROM files ORDER BY id ASC")
        return self.cursor.fetchall()

    def get_latest_file_id(self):
        self.cursor.execute("SELECT MAX(id) FROM files")
        result = self.cursor.fetchone()
        return result[0] if result else None
