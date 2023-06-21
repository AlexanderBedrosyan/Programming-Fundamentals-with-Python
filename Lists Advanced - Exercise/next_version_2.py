version = [int(ch) for ch in input().split(".")]
flag = False

for i in range(len(version) - 1, - 1, -1):
    version[i] += 1
    if version[i] > 9:
        version[i] = 0
        flag = True
    else:
        flag = False
    if not flag:
        break

print(*version, sep=".")
