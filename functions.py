import json
from json import JSONDecodeError

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_json_posts():
    """Функция возвращает JSON файл"""
    try:
        with open("posts.json", "r", encoding='utf8') as file:
            dict_posts = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return "Файл не найден"
    else:
        if list(dict_posts):
            return dict_posts
        else:
            "Не удается преобразовать в словарь"


dict_json = get_json_posts()


def search_tag(word):
    """Функция ищет все слова длиннее 2 символов в каждом content"""
    word = [i.lower() for i in word.split(" ")]
    if word:
        list_content = []
        for c in word:
            for n in dict_json:
                if len(c) >= 3:
                    if c in n["content"].lower():
                        list_content.append(n)
                    else:
                        continue
                else:
                    break
        return list_content
    else:
        return False


def is_filename_allowed(filename=None):
    """Проверяет доаустимый формат"""
    extension = filename.split(".")[-1].lower()
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def add_post_json(picture, post):
    """Дабавляет данные поста в JSON"""
    dict_ = dict()
    dict_["pic"] = f"./uploads/images/{picture}"
    dict_["content"] = post
    try:
        dict_json.append(dict_)
    except (FileNotFoundError, JSONDecodeError):
        return "Не удалось открыть файл"
    else:
        with open("posts.json", "w", encoding='utf8') as file:
            json.dump(dict_json, file, indent=2, ensure_ascii=False)
        return dict_json
