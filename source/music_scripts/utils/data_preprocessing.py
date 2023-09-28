import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords

def load_music_data(filepath):
    return pd.read_csv(filepath)

def clean_music_data(data):
    data['Genre'].fillna('Unknown', inplace=True)
    data['Artist'].fillna('Unknown', inplace=True)
    data['Lyrics'].fillna('', inplace=True)
    data['Title'] = data['Title'].str.lower()
    data['Artist'] = data['Artist'].str.lower()
    data['Genre'] = data['Genre'].str.lower()
    data['Lyrics'] = data['Lyrics'].str.lower()
    data.drop_duplicates(subset='ID', keep='first', inplace=True)
    return data

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def normalize_artist_genre(data):
    artist_mapping = {
        'beatles': 'The Beatles',
        'the beatles': 'The Beatles',
        'j.t.': 'Justin Timberlake',
        'jt': 'Justin Timberlake',
        's. carter': 'Jay-Z',
        'hova': 'Jay-Z',
        'slim shady': 'Eminem',
        'the fab four': 'The Beatles',
        'sir paul mccartney': 'Paul McCartney',
        'zep': 'Led Zeppelin',
        'floyd': 'Pink Floyd',
        'stones': 'The Rolling Stones',
        'mj': 'Michael Jackson',
        'queen b': 'Beyoncé',
        'drizzy': 'Drake',
    }

    genre_mapping = {
        'r&b': 'R&B',
        'hip hop': 'Hip-Hop',
        'hip-hop': 'Hip-Hop',
        'rock n roll': 'Rock',
        'rock & roll': 'Rock',
        'synth-pop': 'Pop',
        'indie rock': 'Indie',
        'indie pop': 'Indie',
        'rap': 'Hip Hop',
        'synth-pop': 'Pop',
        'country & western': 'Country',
        'electronica': 'Electronic',
        'dance music': 'Dance',
    }

    data['Artist'] = data['Artist'].replace(artist_mapping)
    data['Genre'] = data['Genre'].replace(genre_mapping)
    return data

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def detect_language(text):
    try:
        return TextBlob(text).detect_language()
    except:
        return 'unknown'

def create_music_combined_feature(data):
    data['Sentiment'] = data['Lyrics'].apply(sentiment_analysis)
    data = normalize_artist_genre(data)
    data['Language'] = data['Lyrics'].apply(detect_language)
    data['combined_feature'] = data['Title'] + ' ' + data['Artist'] + ' ' + data['Genre'] + ' ' + data['Lyrics'].str[:50] + ' ' + data['Sentiment']
    return data

def filter_music_by_rating(data, min_rating=4.0):
    return data[data['Rating'] >= min_rating]

def filter_music_by_language(data, language="english"):
    return data[data['Language'] == language]
