def print_the_result(targets, counter_shots):
    print(f"Shot targets: {counter_shots} -> {' '.join(str(ch) for ch in targets)}")


def shot_on_target(targets, ind, counter_correct_shots):
    if targets[ind] != -1:
        needed_amount = targets[ind]
        counter_correct_shots += 1
        targets[ind] = -1
        for i in range(len(targets)):
            if targets[i] <= needed_amount and targets[i] != -1:
                targets[i] += needed_amount
            elif targets[i] > targets[ind] and targets[i] != -1:
                targets[i] -= needed_amount
    return targets, counter_correct_shots


def shooting_targets(targets):
    counter = 0
    while True:
        command = input()

        if command == "End":
            print_the_result(targets, counter)
            break

        ind = int(command)

        if 0 <= ind < len(targets):
            targets, counter = shot_on_target(targets, ind, counter)
        else:
            continue


targets_list = [int(ch) for ch in input().split(" ")]
shooting_targets(targets_list)
