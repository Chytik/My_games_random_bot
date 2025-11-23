import sqlite3
from pathlib import Path
import io
import json

#folder = Path('./templates/TLOU2')

conn = sqlite3.connect('games_database.db')
cur = conn.cursor()
# cur.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER NOT NULL PRIMARY KEY,
#     expt TEXT DEFAULT '[]'
# )
# ''')

def get_expt(user_id):
    cur.execute("SELECT expt FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    if row and row[0]:
        return json.loads(row[0])
    else:
        cur.execute("INSERT OR IGNORE INTO users (id, expt) VALUES (?, ?)",(user_id, json.dumps([])))
        conn.commit()
        return []

def save_expt(user_id, expt_list):
    cur.execute("INSERT OR REPLACE INTO users (id, expt) VALUES (?, ?)", (user_id, str(expt_list)))
    conn.commit()

# cur.execute('''
# CREATE TABLE IF NOT EXISTS images (
#     name TEXT PRIMARY KEY,
#     img BLOB
# )
# ''')

# for file_path in folder.glob("*.*"):
#     if file_path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
#         cur.execute("INSERT OR IGNORE INTO images (name, img) VALUES (?, ?)",(file_path.name, file_path.read_bytes()))

def get_photo_from_db(filename):
    cur.execute("SELECT img FROM images WHERE name = ?", (filename,))
    row = cur.fetchone()
    photo_file = io.BytesIO(row[0])
    photo_file.name = filename
    photo_file.seek(0)
    return photo_file

conn.commit()
conn.close()