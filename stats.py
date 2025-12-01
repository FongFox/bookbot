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

    # print("==== Check ====")
    # print(char_count_dict)

    return char_count_dict
