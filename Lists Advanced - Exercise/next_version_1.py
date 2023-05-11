version = [int(ch) for ch in input().split(".")]

if version[2] == 9:
    if version[1] == 9:
        version[1] = 0
        version[2] = 0
        version[0] += 1
    else:
        version[1] += 1
        version[2] = 0
else:
    version[2] += 1

for i in range(len(version)):
    if i == len(version) - 1:
        print(version[i])
    else:
        print(version[i], end=".")