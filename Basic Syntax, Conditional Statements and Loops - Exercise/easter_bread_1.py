budget = float(input())
price_kg_flour = float(input())

price_pack_eggs = price_kg_flour * 0.75
price_quarter_milk = (price_kg_flour * 1.25) * 0.25

total_price_loaf = price_kg_flour + price_pack_eggs + price_quarter_milk

loaves_total = budget // total_price_loaf

colored_eggs = 0
loaves_counter = 0

for i in range(1, int(loaves_total) + 1):
    colored_eggs += 3
    loaves_counter += 1
    if i % 3 == 0:
        colored_eggs -= (loaves_counter - 2)

print(f"You made {int(loaves_total)} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {budget - (total_price_loaf * loaves_total):.2f}BGN left.")
