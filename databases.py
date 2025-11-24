import sqlite3
from pathlib import Path
import io, os
import json

#folder = Path('./templates/TLOU2')

DB_PATH = 'games_database.db'


def get_expt(user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT expt FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row and row['expt']:
        return json.loads(row['expt'])
    else:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (id, expt) VALUES (?, ?)", (user_id, json.dumps([])))
        conn.commit()
        conn.close()
        return []


def save_expt(user_id, expt_list):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO users (id, expt) VALUES (?, ?)", (user_id, json.dumps(expt_list)))
    conn.commit()
    conn.close()

def get_photo_from_db(filename):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT img FROM images WHERE name = ?", (filename,))
    row = cur.fetchone()
    conn.close()

    if not row:
        raise FileNotFoundError(f"Фото {filename} не найдено в базе!")

    photo_file = io.BytesIO(row['img'])
    photo_file.name = filename
    photo_file.seek(0)
    return photo_file

# conn = sqlite3.connect('games_database.db', check_same_thread=False)
# cur = conn.cursor()
# cur.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER NOT NULL PRIMARY KEY,
#     expt TEXT DEFAULT '[]'
# )
# ''')



# def save_expt(user_id, expt_list):
#     cur.execute("INSERT OR REPLACE INTO users (id, expt) VALUES (?, ?)", (user_id, str(expt_list)))
#     conn.commit()

# cur.execute('''
# CREATE TABLE IF NOT EXISTS images (
#     name TEXT PRIMARY KEY,
#     img BLOB
# )
# ''')

# for file_path in folder.glob("*.*"):
#     if file_path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
#         cur.execute("INSERT OR IGNORE INTO images (name, img) VALUES (?, ?)",(file_path.name, file_path.read_bytes()))

# def get_photo_from_db(filename):
#     cur.execute("SELECT img FROM images WHERE name = ?", (filename,))
#     row = cur.fetchone()
#     photo_file = io.BytesIO(row[0])
#     photo_file.name = filename
#     photo_file.seek(0)
#     return photo_file
#
# conn.commit()
# conn.close()


DB_FILE = 'user_data.json'
_cache = json.load(open(DB_FILE, 'r')) if os.path.exists(DB_FILE) else {}
def load_db():
    global _cache
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            _cache = json.load(f)
def save_db():
    with open(DB_FILE, 'w') as f:
        json.dump(_cache, f, indent=2, ensure_ascii=False)