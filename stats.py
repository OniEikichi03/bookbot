def count_words(contents):
    words = contents.split()
    return len(words)

def count_characters(contents):
    chars = {}
    content = contents.lower()
    for character in content:
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1
    return chars

def sort_on(item):
    return item["num"]

def split_dict(chars):
    results = []
    for char in chars:
        if char.isalpha():
            new_dict = {"char": char, "num": chars[char]}
            results.append(new_dict)
    results.sort(reverse=True, key=sort_on)
    return results



    

