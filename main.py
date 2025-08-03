import sys
from stats import count_words, read_character_counts, sorted_character_counts

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def read_book(file_name):
    content = get_book_text(file_name)
    count = count_words(content)
    character_counts = read_character_counts(content)
    sorted_counts = sorted_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    read_book(sys.argv[1])

main()
