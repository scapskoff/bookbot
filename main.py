import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        count_words(text)
        print("--------- Character Count -------")
        for item in sorted_list(count_characters(text)):
            char = item["char"]
            count = item["count"]
            if not char.isalpha():
                continue
            else:
                print(f"{char}: {count}")
        print("============= END ===============")
main()