def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)

main()