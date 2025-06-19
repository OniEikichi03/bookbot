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

def split_dict(chars):
    results = []
    for char in chars:
        new_dict = {"char": char, "num": chars[char]}
        results.append(chars[char])
    pass
    

