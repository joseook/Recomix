from sklearn.metrics.pairwise import cosine_similarity

def compute_anime_similarity_matrix(embeddings):
    matrix = list(embeddings.values())
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix

def get_anime_recommendations(title, data, similarity_matrix):
    idx = data.index[data['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    anime_indices = [i[0] for i in sim_scores]
    return data['Title'].iloc[anime_indices]

def get_genre_based_recommendations(genre, data, top_n=10):
    return data[data['Genres'].apply(lambda x: genre in x)].nlargest(top_n, 'Rating')['Title'].tolist()

def get_personalized_recommendations(user_watched_list, user_ratings, data, similarity_matrix):

    watched_indices = [data.index[data['Title'] == anime].tolist()[0] for anime in user_watched_list]


    recommendation_scores = [0] * len(data)


    for idx, anime in enumerate(user_watched_list):
        anime_index = watched_indices[idx]
        rating = user_ratings[anime]
        for j, score in enumerate(similarity_matrix[anime_index]):
            recommendation_scores[j] += score * rating


    recommended_indices = sorted(range(len(recommendation_scores)), key=lambda i: recommendation_scores[i], reverse=True)[:10]


    return data['Title'].iloc[recommended_indices].tolist()

def get_top_n_recommendations(n, data, similarity_matrix):
    recommendations = []
    for idx in range(len(similarity_matrix)):
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:n+1]
        anime_indices = [i[0] for i in sim_scores]
        recommendations.append(data['Title'].iloc[anime_indices].tolist())
    return recommendations
