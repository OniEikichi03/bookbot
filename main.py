import sys
from stats import count_words, count_characters, split_dict, sort_on


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        contents = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    characters = count_characters(contents)
    print("--------- Character Count -------")
    new_dict = split_dict(characters)
    for item in new_dict:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()
