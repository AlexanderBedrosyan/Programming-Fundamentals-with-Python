def is_valid(ticket):
    if len(ticket) == 20:
        return True
    return False


def is_jackpot(ticket, symbols):
    if not is_valid(ticket):
        return False
    for ch in symbols:
        if ticket.count(ch) == 20:
            return True
    return False


def is_winning(ticket, symbols):
    if not is_valid(ticket):
        return False

    global uninterrupted_match_length
    global match_symbol

    left_part = ticket[:10]
    right_part = ticket[10:]
    letter = ''
    current_word = ''
    while left_part:
        current_letter = left_part[0]
        if current_letter in symbols:
            if len(letter) == 0:
                current_word = current_letter
                letter = current_letter
            elif letter == current_letter:
                current_word += current_letter
            else:
                if len(current_word) >= 6:
                    while len(current_word) >= 6:
                        if current_word in right_part and len(current_word) >= 6:
                            uninterrupted_match_length = len(current_word)
                            match_symbol = letter
                            return True
                else:
                    letter = current_letter
                    current_word = current_letter

        left_part = left_part[1:]
    while len(current_word) >= 6:
        if current_word in right_part and len(current_word) >= 6:
            uninterrupted_match_length = len(current_word)
            match_symbol = letter
            return True
        current_word = current_word[:-1]
    return False


def final_result(tickets):
    gather_the_results = []
    needed_characters = ["@", "#", "$", "^"]

    for ticket in tickets:
        ticket = ticket.strip()
        if not is_valid(ticket):
            gather_the_results.append("invalid ticket")
        elif not is_jackpot(ticket, needed_characters) and not is_winning(ticket, needed_characters):
            gather_the_results.append(f'ticket "{ticket}" - no match')
        elif is_winning(ticket, needed_characters) and not is_jackpot(ticket, needed_characters):
            gather_the_results.append(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
        elif is_winning(ticket, needed_characters) and is_jackpot(ticket, needed_characters):
            gather_the_results.append(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')

    return '\n'.join(gather_the_results)


tickets = input().split(", ")
print(final_result(tickets))
