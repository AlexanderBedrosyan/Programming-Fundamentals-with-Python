def text_filter(list_words, editing_text):
    new_text = editing_text
    for i in range(len(list_words)):
        while list_words[i] in new_text:
            new_text = new_text.replace(list_words[i], len(list_words[i]) * "*")
    return new_text


word = input().split(", ")
text = input()
print(text_filter(word, text))
