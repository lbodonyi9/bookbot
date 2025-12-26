def word_count(text):
    words = text.split()
    return len(words)

def num_of_each_character(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_char_count(text):
    char_count = num_of_each_character(text)
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():  # Consider only alphabetic characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list