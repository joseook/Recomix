from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from gensim.models import Word2Vec

def compute_music_tfidf_features(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_feature'])
    return tfidf_matrix

def compute_music_similarity_matrix(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)

def create_music_embeddings(data):
    sentences = [row.split() for row in data['Lyrics']]
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    model.save("music_word2vec.model")
    
    embeddings = {}
    for index, row in data.iterrows():
        vector = sum([model.wv[word] for word in row['Lyrics'].split()]) / len(row['Lyrics'].split())
        embeddings[row['Title']] = vector
    
    return embeddings

def get_music_recommendations(title, data, similarity_matrix):
    idx = data.index[data['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    music_indices = [i[0] for i in sim_scores]
    return data['Title'].iloc[music_indices]
