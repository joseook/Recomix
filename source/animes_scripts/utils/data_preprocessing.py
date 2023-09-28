import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.preprocessing import MinMaxScaler

def load_anime_data(file_path):
    return pd.read_csv(file_path)

def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def normalize_text(text):
    words = text.split()
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english')]
    return ' '.join(words)

def clean_anime_data(data):
    data = data.dropna(subset=['Title', 'Genres', 'Synopsis'])
    data['Synopsis'] = data['Synopsis'].apply(remove_special_characters)
    data['Synopsis'] = data['Synopsis'].apply(normalize_text)
    data['combined_feature'] = data['Title'] + ' ' + data['Genres'] + ' ' + data['Synopsis']
    return data

def scale_data(data, columns):
    scaler = MinMaxScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data
