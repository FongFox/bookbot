def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        # f is a file object
        file_contents = f.read()
    f.closed

    return file_contents


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(book_contents)
    pass


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
