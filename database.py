import sqlite3

def get_connection():
    conn = sqlite3.connect("quiz.db")
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()


def clear_questions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM questions")

    conn.commit()
    conn.close()


def insert_question(q, a, b, c, d, ans):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO questions(question,option_a,option_b,option_c,option_d,answer)
    VALUES(?,?,?,?,?,?)
    """, (q, a, b, c, d, ans))

    conn.commit()
    conn.close()


def get_questions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")

    data = cursor.fetchall()

    conn.close()

    return data