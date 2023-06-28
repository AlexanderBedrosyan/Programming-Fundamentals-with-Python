def result(legendary_item, materials, junk, winner):
    final_result = []
    final_result.append(f"{legendary_item[winner]} obtained!")
    for elements, amount in materials.items():
        final_result.append(f"{elements}: {amount}")
    if junk:
        for elements, amount in junk.items():
            final_result.append(f"{elements}: {amount}")
    return '\n'.join(final_result)


def GetResult(materials):
    junk = {}
    win_a_legendary_item = ''
    condition = False

    while True:
        command = [ch.lower() for ch in input().split(" ")]
        for i in range(0, len(command), 2):
            material = command[i + 1]
            quantity = int(command[i])

            if material not in materials:
                if material not in junk:
                    junk[material] = 0
                junk[material] += quantity
            else:
                materials[material] += quantity
                if materials[material] >= 250:
                    win_a_legendary_item = material
                    materials[win_a_legendary_item] -= 250
                    condition = True
                    break
        if condition:
            break

    return result(legendary_item, materials, junk, win_a_legendary_item)


legendary_item = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
materials = {"shards": 0, "fragments": 0, "motes": 0}
print(GetResult(materials))
