import re

collection_of_eggs = input()
pattern = r"([@#]+)([a-z]{3,})([@#]+)([^\w\d]+)?([\/]+)([0-9]+)([\/]+)"
matches = re.findall(pattern, collection_of_eggs)

for current_tuple in matches:
    if int(current_tuple[5]) == 0:
        continue
    print(f"You found {current_tuple[5]} {current_tuple[1]} eggs!")
