import pandas as pd
from PyInquirer import prompt
from utils.data_preprocessing import load_anime_data, clean_anime_data, split_genres
from utils.feature_extraction import create_anime_embeddings, compute_tfidf_matrix
from utils.model import compute_anime_similarity_matrix, get_anime_recommendations, get_genre_based_recommendations, get_personalized_recommendations
from utils.input_validators import RatingValidator, AnimeTitleValidator, GenreValidator, AnimeListValidator
from styles.menu_style_animes import style

def display_header():
    print("\n===================================")
    print("= Sistema de Recomendação de Animes=")
    print("===================================\n")

def display_footer():
    print("\n===================================")
    print("= Obrigado por usar nosso sistema! =")
    print("===================================\n")

def display_menu():
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Escolha uma opção:',
            'choices': [
                {'name': 'Recomendar animes baseado em título', 'value': '1'},
                {'name': 'Recomendar animes baseado em gênero', 'value': '2'},
                {'name': 'Recomendações personalizadas', 'value': '3'},
                {'name': 'Sair', 'value': '4'}
            ],
            'default': '1'
        }
    ]
    answers = prompt(questions, style=style)
    return answers['choice']

def main():
    # Carregar e pré-processar os dados
    data = load_anime_data("data/raw/anime_dataset.csv")
    data = clean_anime_data(data)
    data = split_genres(data)
    
    # Extração de características
    embeddings = create_anime_embeddings(data)
    tfidf_matrix = compute_tfidf_matrix(data)
    
    # Calcular matriz de similaridade
    similarity_matrix = compute_anime_similarity_matrix(embeddings)

    anime_titles = data['Title'].tolist()
    genres = set(data['Genres'].explode().tolist())

    while True:
        display_header()
        choice = display_menu()
        if choice == "1":
            questions = [
                {
                    'type': 'input',
                    'name': 'title',
                    'message': "Digite o título de um anime que você gosta:",
                    'validate': AnimeTitleValidator(anime_titles)
                }
            ]
            answers = prompt(questions, style=style)
            title = answers['title']
            recommended_animes = get_anime_recommendations(title, data, similarity_matrix)
            print("\nRecomendações:")
            for anime in recommended_animes:
                print(anime)
        elif choice == "2":
            questions = [
                {
                    'type': 'input',
                    'name': 'genre',
                    'message': "Digite um gênero que você gosta:",
                    'validate': GenreValidator(genres)
                }
            ]
            answers = prompt(questions, style=style)
            genre = answers['genre']
            recommended_animes = get_genre_based_recommendations(genre, data)
            print("\nRecomendações:")
            for anime in recommended_animes:
                print(anime)
        elif choice == "3":
            questions = [
                {
                    'type': 'input',
                    'name': 'user_watched_list',
                    'message': "Digite uma lista de animes que você já assistiu (separados por vírgula):",
                    'validate': AnimeListValidator(anime_titles)
                }
            ]
            answers = prompt(questions, style=style)
            user_watched_list = answers['user_watched_list'].split(',')
            user_ratings = {}
            for anime in user_watched_list:
                rating_question = [
                    {
                        'type': 'input',
                        'name': 'rating',
                        'message': f"Classifique o anime '{anime}' (1-5):",
                        'validate': RatingValidator
                    }
                ]
                rating_answer = prompt(rating_question, style=style)
                user_ratings[anime.strip()] = float(rating_answer['rating'])
            recommended_animes = get_personalized_recommendations(user_watched_list, user_ratings, data, similarity_matrix)
            print("\nRecomendações personalizadas:")
            for anime in recommended_animes:
                print(anime)
        elif choice == "4":
            display_footer()
            break

if __name__ == "__main__":
    main()
