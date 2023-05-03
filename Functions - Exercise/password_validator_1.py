def password_validator(password):
    new_password = [ch for ch in password]
    ch_counter = 0
    letters_counter = 0
    digits = 0
    not_included = 0

    for letters in new_password:
        ch_counter += 1
        if 65 <= ord(letters) <= 90 or 97 <= ord(letters) <= 122:
            letters_counter += 1
        elif 48 <= ord(letters) <= 57:
            digits += 1
        else:
            not_included += 1

    if ch_counter == (letters_counter + digits) and 6 <= ch_counter <= 10 and digits >= 2:
        print("Password is valid")
    else:
        if 6 > ch_counter or ch_counter > 10:
            print("Password must be between 6 and 10 characters")
        if not_included > 0:
            print("Password must consist only of letters and digits")
        if digits < 2:
            print("Password must have at least 2 digits")


password = input()

password_validator(password)
