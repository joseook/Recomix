import sqlite3

def create_feedback_database():
    conn = sqlite3.connect('music_feedback.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback
                     (music TEXT, rating INTEGER, comment TEXT)''')
    conn.commit()
    conn.close()

def store_feedback_in_database(feedback_data):
    conn = sqlite3.connect('music_feedback.db')
    cursor = conn.cursor()
    for music, feedback in feedback_data.items():
        cursor.execute("INSERT INTO feedback (music, rating, comment) VALUES (?, ?, ?)", (music, feedback['rating'], feedback['comment']))
    conn.commit()
    conn.close()

def retrieve_feedback_from_database():
    conn = sqlite3.connect('music_feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedback_data = cursor.fetchall()
    conn.close()
    return feedback_data
