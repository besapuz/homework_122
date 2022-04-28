import json


def get_json_posts():
    with open("posts.json", "r", encoding='utf8') as file:
        dict_posts = json.load(file)
    return dict_posts


dict_json = get_json_posts()


def search_tag(word):
    if word:
        list_content = []
        s = ''.join(word.split())
        for i in dict_json:
            if s in i["content"]:
                list_content.append(i)
        return list_content
    else:
        return False


