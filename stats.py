def count_words(content):
    words = content.split()
    return len(words)

def read_character_counts(content):
    character_counts = dict()
    for character in content:
        check = character.lower()
        if check in character_counts:
            character_counts[check] = { "char": check, "count": character_counts[check]["count"] + 1 }
        else:
            character_counts[check] = { "char": check, "count": 1 } 
    return character_counts

def sort_by_count(counts):
    return counts["count"]

def sorted_character_counts(counts):
    sorted = list(counts.values())
    sorted.sort(reverse=True, key=sort_by_count)
    return sorted
