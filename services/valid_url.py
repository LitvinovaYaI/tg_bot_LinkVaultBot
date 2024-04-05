import re


def is_valid_url(text: str) -> bool:
    """
    Проверка, является ли строка ссылкой
    """
    try:
        url_pattern = re.compile(
            r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
        )
        return bool(url_pattern.match(text.strip()))
    except ValueError:
        return False
