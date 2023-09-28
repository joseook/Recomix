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

class AnimeTitleValidator(Validator):
    def __init__(self, anime_list):
        self.anime_list = anime_list

    def validate(self, document):
        if document.text not in self.anime_list:
            raise ValidationError(
                message='Por favor, insira um título de anime válido da lista',
                cursor_position=len(document.text)
            )

class GenreValidator(Validator):
    def __init__(self, genre_list):
        self.genre_list = genre_list

    def validate(self, document):
        if document.text not in self.genre_list:
            raise ValidationError(
                message='Por favor, insira um gênero válido da lista',
                cursor_position=len(document.text)
            )

class AnimeListValidator(Validator):
    def __init__(self, anime_list):
        self.anime_list = anime_list

    def validate(self, document):
        user_animes = [anime.strip() for anime in document.text.split(',')]
        for anime in user_animes:
            if anime not in self.anime_list:
                raise ValidationError(
                    message=f"'{anime}' não é um título de anime válido. Por favor, insira títulos válidos.",
                    cursor_position=len(document.text)
                )
