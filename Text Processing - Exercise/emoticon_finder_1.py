def emoticon_finder(text):
    emoticons = []

    for i in range(len(text)):
        if text[i] == ":":
            emoji = text[i] + text[i + 1]
            emoticons.append(emoji)

    return emoticons


current_text = [str(ch) for ch in input()]

print(*emoticon_finder(current_text), sep="\n")