from stats import count_words


def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        # f is a file object
        file_contents = f.read()
    f.closed

    return file_contents


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)

    print(f"Found {num_words} total words")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
