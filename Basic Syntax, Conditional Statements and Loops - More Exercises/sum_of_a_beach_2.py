def counter(needed_words, current_string):
    counter = 0
    for ch in needed_words:
        while ch in current_string:
            counter += 1
            current_string = current_string.replace(ch, "", 1)
    return counter


needed_words = ["water", "fish", "sun", "sand"]
current_string = input().lower()

print(counter(needed_words, current_string))
