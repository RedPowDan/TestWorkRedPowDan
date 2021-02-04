

def parsing(string: str) -> dict:
    words = string.split()
    words.pop(0)
    words.pop(0)
    words.pop(3)
    date = words.pop(0)
    words[0] = date + " " + words[0]
    words[1] = words[1].replace("[", "")
    words[1] = words[1].replace("]", "")

    dict_words = {'date': words[0],
                  'id_string': words[1],
                  'IP': words[2],
                  'link': words[3]}

    return dict_words
