import sys

from stats import count_character, count_words, sort_character


def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        # f is a file object
        file_contents = f.read()
    f.closed

    return file_contents


def print_report(book_file_path):
    # book_file_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_file_path)
    num_words = count_words(book_contents)
    num_character_dict = count_character(book_contents)
    num_character_list = sort_character(num_character_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_character(num_character_dict)
    # print(num_character_dict)
    # print(num_character_list)
    for num_char in num_character_list:
        if num_char["name"].isalpha():
            print(f"{num_char['name']}: {num_char['num']}")
        else:
            continue
    print("============= END ===============")


def main():
    sys_argv_len = len(sys.argv) - 1
    if sys_argv_len < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
