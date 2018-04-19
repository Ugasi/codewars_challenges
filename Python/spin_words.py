def spin_words(sentence):
    for word in sentence.split(" "):
        if len(word) > 4:
            sentence = sentence.replace(word, word[::-1], 1)
    return sentence
spin_words("Welcome")