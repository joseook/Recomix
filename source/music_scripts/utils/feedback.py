from source.music_scripts.utils.database.database_operations import store_feedback_in_database
from utils.database.database_operations import store_feedback_in_database
def collect_music_feedback(recommended_music):
    feedback_data = {}
    for music in recommended_music:
        rating = input(f"Por favor, avalie a música '{music}' de 1 a 5: ")
        comment = input(f"Comentários sobre a música '{music}': ")
        feedback_data[music] = {'rating': rating, 'comment': comment}
    store_feedback_in_database(feedback_data)
    return feedback_data
