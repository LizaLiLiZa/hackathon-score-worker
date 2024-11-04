import re

def is_valid_russian_text(text):
    """Проверяет, содержатся ли в строке символы кроме кириллических, цифр, пробелов и пунктуации"""
    pattern = r'^[А-Яа-яЁё0-9\s\-\[\];,:.@#$%&*()/_+]+$'
    return bool(re.fullmatch(pattern, text))