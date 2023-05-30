from collections import deque


def find_first_second_list(first_list, second_list, cards):
    current_list = deque([ch for ch in cards])
    while len(current_list) > 0:
        if len(current_list) > (len(cards) / 2):
            first_list.append(current_list.popleft())
        else:
            second_list.append(current_list.popleft())
    return first_list, second_list


def new_cards(first_list, second_list):
    new_cards_list = []
    while len(second_list) > 0:
        ch1 = first_list.popleft()
        ch2 = second_list.popleft()
        new_cards_list.append(ch1)
        new_cards_list.append(ch2)
    return new_cards_list


cards = input().split(" ")
rows = int(input())
first_list = deque()
second_list = deque()

for _ in range(rows):
    first_list, second_list = deque(), deque()
    first_list, second_list = find_first_second_list(first_list, second_list, cards)
    cards = new_cards(first_list, second_list)

print(cards)
