
def get_music_recommendations(title, data, similarity_matrix):
    idx = data.index[data['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    music_indices = [i[0] for i in sim_scores]
    return data['Title'].iloc[music_indices]

def get_music_recommendations_by_artist(artist, data, top_n=10):
    return data[data['Artist'] == artist].nlargest(top_n, 'Rating')['Title'].tolist()

def get_music_recommendations_by_genre(genre, data, top_n=10):
    return data[data['Genre'] == genre].nlargest(top_n, 'Rating')['Title'].tolist()

def get_personalized_music_recommendations(user_listened_list, user_ratings, data, similarity_matrix):
    listened_indices = [data.index[data['Title'] == music].tolist()[0] for music in user_listened_list]
    recommendation_scores = [0] * len(data)
    
    for idx, music in enumerate(user_listened_list):
        music_index = listened_indices[idx]
        rating = user_ratings[music]
        for j, score in enumerate(similarity_matrix[music_index]):
            recommendation_scores[j] += score * rating
    
    recommended_indices = sorted(range(len(recommendation_scores)), key=lambda i: recommendation_scores[i], reverse=True)[:10]
    return data['Title'].iloc[recommended_indices].tolist()

def get_music_recommendations_by_sentiment(sentiment, data, top_n=10):
    return data[data['Sentiment'] == sentiment].nlargest(top_n, 'Rating')['Title'].tolist()
