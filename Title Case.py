import re
def title_case(title, minor_words=''):
    word_list = re.split(' ', title.lower())
    end = [word_list[0].capitalize()]
    for word in word_list[1:]:
        end.append(word if word in minor_words.lower().split() else word.capitalize())
    return " ".join(end)
