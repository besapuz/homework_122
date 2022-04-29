import json
from json import JSONDecodeError

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_json_posts():
    """Функция возвращает JSON файл"""
    with open("posts.json", "r", encoding='utf8') as file:
        dict_posts = json.load(file)
    return dict_posts
    #except JSONDecodeError:
        #return "Не удалось открыть файл

dict_json = get_json_posts()


def search_tag(word):
    word = str(word).lower()
    if word:
        list_content = []
        s = ''.join(word.split())
        for i in dict_json:
            if s in i["content"].lower():
                list_content.append(i)
        return list_content
    elif word is None:
        return None
    else:
        return False


def is_filename_allowed(filename=None):
    extension = filename.split(".")[-1].lower()
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def add_post_json(picture, post):

    with open("posts.json", "r", encoding='utf8') as file:
        dict_json = json.load(file)
    dict_ = {}
    list_ = []
    dict_["pic"] = f"./uploads/images/{picture}"
    dict_["content"] = post
    list_.append(dict_)
    with open("posts.json", "a", encoding='utf8') as file:
        json.dump(dict_, file, indent=2, ensure_ascii=False)
    return dict_json



#print(add_post_json("ключ", "dsvsdvsd"))
