def count_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def count_characters(text):
    character_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in character_counts:
            character_counts[f"{lowercase_char}"] += 1
        else:
            character_counts[f"{lowercase_char}"] = 1
    return character_counts

def sorted_list(character_counts):
    def sort_on(items):
        return items["count"]
    list = []
    for item in character_counts:
        list.append({"char": item, "count": character_counts[item]})
    
    list.sort(reverse=True, key=sort_on)
    return list