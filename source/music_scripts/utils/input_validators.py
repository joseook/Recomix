
from PyInquirer import Validator, ValidationError

class RatingValidator(Validator):
    def validate(self, document):
        try:
            if 1 <= int(document.text) <= 5:
                return True
            else:
                raise ValidationError(
                    message='Por favor, insira um número entre 1 e 5',
                    cursor_position=len(document.text)
                )
        except ValueError:
            raise ValidationError(
                message='Por favor, insira um número válido',
                cursor_position=len(document.text)
            )

class SentimentValidator(Validator):
    def validate(self, document):
        valid_sentiments = ["positive", "neutral", "negative"]
        if document.text.lower() not in valid_sentiments:
            raise ValidationError(
                message='Por favor, insira um sentimento válido (positive, neutral, negative)',
                cursor_position=len(document.text)
            )

def validate_music_title(title, data):
    """Verifica se o título da música fornecido pelo usuário existe no conjunto de dados."""
    return title in data['Title'].values

def validate_genre(genre, data):
    """Verifica se o gênero fornecido pelo usuário existe no conjunto de dados."""
    return genre.lower() in data['Genre'].str.lower().unique()

def validate_artist(artist, data):
    """Verifica se o artista fornecido pelo usuário existe no conjunto de dados."""
    return artist.lower() in data['Artist'].str.lower().values

def validate_comment(comment):
    """Verifica se o comentário fornecido pelo usuário não está vazio e não excede um limite de caracteres."""
    MAX_COMMENT_LENGTH = 500
    return 0 < len(comment) <= MAX_COMMENT_LENGTH

def validate_language(language, supported_languages):
    """Verifica se o idioma fornecido pelo usuário é suportado."""
    return language.lower() in supported_languages
