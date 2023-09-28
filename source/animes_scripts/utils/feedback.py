import sqlite3
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
import pandas as pd


def collect_user_feedback(recommended_animes):
    feedback_data = {}
    for anime in recommended_animes:
        rating = input(f"Por favor, avalie o anime '{anime}' de 1 a 5: ")
        comment = input(f"Comentários sobre o anime '{anime}': ")
        feedback_data[anime] = {'rating': rating, 'comment': comment}
    return feedback_data

def store_feedback_in_db(feedback_data, db_path="database/feedback.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for anime, feedback in feedback_data.items():
        cursor.execute("INSERT INTO feedback (anime, rating, comment) VALUES (?, ?, ?)", (anime, feedback['rating'], feedback['comment']))
    conn.commit()
    conn.close()

def load_feedback_from_db(db_path='database/feedback.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    feedback_data = cursor.execute('SELECT * FROM feedback').fetchall()
    conn.close()
    return feedback_data

def create_feedback_model(input_dim):
    model = Sequential()
    model.add(Dense(128, activation='relu', input_dim=input_dim))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_feedback_model_with_data(model, feedback_data):

    df = pd.DataFrame(feedback_data)
    X = np.stack(df['features'].values)
    y = df['rating'].values
    y = to_categorical(y)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    return model

def adjust_recommendations_based_on_feedback(recommended_animes, feedback_data):
    return [anime for anime in recommended_animes if int(feedback_data[anime]['rating']) > 3]
