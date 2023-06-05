n = int(input())
m = input()

list_m = []
count = 0

for i in range(0, len(m) + 1):
    if i % 2 == 0:
        list_m.append(m[i])
    else:
        continue

for i in range(0, len(list_m)):
    if int(list_m[i]) <= 4:
        if (n + int(list_m[i])) < 4:
            list_m[i] = n + int(list_m[i])
            n = 0
            break
        elif (n + int(list_m[i])) == 4:
            list_m[i] = n + int(list_m[i])
            n = 0
            count += 1
            break
        else:
            n -= (4 - int(list_m[i]))
            list_m[i] = 4
    else:
        continue

if n > 0:
    print(f"There isn't enough space! {n} people in a queue!")
    print(*list_m)
elif (n == 0) and (count == 1) and (list_m[len(list_m) - 1] == 4):
    print(*list_m)
elif (n == 0) and (count == 1) and (int(list_m[len(list_m) - 1]) < 4):
    print(f"The lift has empty spots!")
    print(*list_m)
elif (n == 0) and (count == 0):
    print(f"The lift has empty spots!")
    print(*list_m)