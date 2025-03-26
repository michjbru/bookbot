def count_words(text):
    words = text.split()
    return len(words)

def count_characters(letters):
    lowercase = letters.lower()
    char_counts = {}
    for char in lowercase:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_order(dict):
    return dict["count"]

def chars_to_sorted_list(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
        chars_list.sort(reverse=True, key=sort_order)
    return chars_list