def single_root_words(root_word, *other_words):
    same_words = list()
    root_word_lower = root_word.lower()
    word = list(other_words)
    word_lower = [s.lower() for s in word]
    for i in range(len(word_lower)):
        if root_word_lower in word_lower[i] or root_word_lower.count(word_lower[i]):
            same_words.append(word[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
