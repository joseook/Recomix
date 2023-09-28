from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

def create_anime_embeddings(data):
    sentences = [row.split() for row in data['combined_feature']]
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    model.save("anime_word2vec.model")
    
    embeddings = {}
    for index, row in data.iterrows():
        vector = sum([model.wv[word] for word in row['combined_feature'].split()]) / len(row['combined_feature'].split())
        embeddings[row['Title']] = vector
    return embeddings

def compute_tfidf_matrix(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_feature'])
    return tfidf_matrix

def reduce_dimensions(matrix, dimensions=50):
    pca = PCA(n_components=dimensions)
    reduced_matrix = pca.fit_transform(matrix)
    return reduced_matrix
