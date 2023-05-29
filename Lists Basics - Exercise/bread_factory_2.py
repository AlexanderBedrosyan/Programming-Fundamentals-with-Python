def rest(current_energy, total_energy):
    total_energy += current_energy
    if total_energy > 100:
        current_energy -= (total_energy - 100)
        total_energy = 100
    print(f"You gained {current_energy} energy.")
    print(f"Current energy: {total_energy}.")
    return total_energy


def order(total_coins, total_energy, amount):
    if 30 <= total_energy:
        total_energy -= 30
        total_coins += amount
        print(f"You earned {amount} coins.")
    else:
        total_energy += 50
        if total_energy > 100:
            total_energy = 100
        print("You had to rest!")
    return total_coins, total_energy


def other_cases(amount, total_coins, ingredient):
    flag = True
    if amount <= total_coins:
        print(f"You bought {ingredient}.")
        total_coins -= amount
    else:
        print(f"Closed! Cannot afford {ingredient}.")
        flag = False
    return flag, total_coins


energy = 100
coins = 100
events = input().split("|")
flag = True

for i in range(len(events)):
    option, quantity = events[i].split("-")

    if option == "rest":
        energy = rest(int(quantity), energy)
    elif option == "order":
        coins, energy = order(coins, energy, int(quantity))
    else:
        flag, coins = other_cases(int(quantity), coins, option)
        if not flag:
            break

if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
