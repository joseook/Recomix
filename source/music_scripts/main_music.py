import pandas as pd
from source.music_scripts.utils.model import collaborative_filtering_recommendations, get_music_recommendations_by_artist
from utils.data_preprocessing import load_music_data, clean_music_data, create_music_combined_feature
from utils.feature_extraction import compute_music_tfidf_features, compute_music_similarity_matrix, get_music_recommendations
from utils.input_validators import TitleValidator, RatingValidator, SentimentValidator
from PyInquirer import prompt

def display_menu():
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Menu de Opções:',
            'choices': [
                'Recomendar músicas baseado em título',
                'Recomendação baseada em filtragem colaborativa',
                'Recomendar músicas baseado em sentimento',
                'Sair'
            ]
        }
    ]
    answers = prompt(questions)
    return answers['choice']

def get_user_input(message, validator):
    questions = [{'type': 'input', 'name': 'value', 'message': message, 'validate': validator}]
    answers = prompt(questions)
    return answers['value']

def display_recommendations(recommendations, message="\nRecomendações:"):
    print(message)
    for music in recommendations:
        print(music)

def handle_user_interaction(data, similarity_matrix):
    choice = display_menu()
    if choice == 'Recomendar músicas baseado em título':
        title = get_user_input("Digite o título de uma música que você gosta:", TitleValidator)
        recommended_music = get_music_recommendations(title, data, similarity_matrix)
        display_recommendations(recommended_music)

    elif choice == 'Recomendação baseada em filtragem colaborativa':
        title = get_user_input("Digite o título de uma música que você gosta:", TitleValidator)
        recommended_music = collaborative_filtering_recommendations(title, data, similarity_matrix)
        display_recommendations(recommended_music, "Recomendações baseadas em filtragem colaborativa:")

    elif choice == 'Recomendar músicas baseado em sentimento':
        sentiment = get_user_input("Digite o sentimento (positive, neutral, negative):", SentimentValidator)
        recommended_music = get_music_recommendations_by_artist(sentiment, data)
        display_recommendations(recommended_music, f"\nRecomendações para músicas com sentimento {sentiment}:")

    elif choice == 'Sair':
        print("Obrigado por usar o sistema de recomendação!")

def main():
    data = load_music_data("data/raw/music_dataset.csv")
    data = clean_music_data(data)
    data = create_music_combined_feature(data)
    tfidf_matrix = compute_music_tfidf_features(data)
    similarity_matrix = compute_music_similarity_matrix(tfidf_matrix)

    while True:
        handle_user_interaction(data, similarity_matrix)

if __name__ == "__main__":
    main()
