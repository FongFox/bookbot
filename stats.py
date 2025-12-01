def count_words(content):
    words = content.split()

    return len(words)


def count_character(content):
    char_count_dict = {}

    for char in content:
        char_lower = char.lower()
        if char_lower in char_count_dict:
            char_count_dict[char_lower] = char_count_dict[char_lower] + 1
        else:
            char_count_dict[char_lower] = 1

    return char_count_dict


def convert_dict_to_list(item_dict):
    item_list = []
    for key in item_dict.keys():
        temp_dict = {"name": key, "num": item_dict[key]}
        item_list.append(temp_dict)

    return item_list


def sort_on(items):
    return items["num"]


def sort_character(char_count_dict):
    char_count_list = convert_dict_to_list(char_count_dict)
    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list
