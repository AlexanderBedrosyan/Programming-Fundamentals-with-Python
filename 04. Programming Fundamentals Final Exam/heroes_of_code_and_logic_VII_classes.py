class Heroes:
    MAX_HP = 100
    MAX_MP = 200

    def __init__(self, number):
        self.number = number
        self.heroes = {}

    def fill_the_heroes(self):
        for _ in range(self.number):
            current_hero, hp, mp = input().split(" ")
            if current_hero not in self.heroes:
                self.heroes[current_hero] = {}
                self.heroes[current_hero][int(hp)] = int(mp)

    def castspell(self, hero_name, mp_needed, spell_name):
        for hp, mana in self.heroes[hero_name].items():
            if mana >= mp_needed:
                self.heroes[hero_name][hp] = (mana - mp_needed)
                print(f"{hero_name} has successfully cast {spell_name} and now has {self.heroes[hero_name][hp]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    def takedamage(self, hero_name, damage, attacker):
        for hp, mana in self.heroes[hero_name].items():
            if hp > damage:
                new_hp = hp - damage
                self.heroes[hero_name] = {}
                self.heroes[hero_name][new_hp] = mana
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {new_hp} HP left!")
            else:
                del self.heroes[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

    def recharge(self, hero_name, amount_mp):
        for hp, mana in self.heroes[hero_name].items():
            rest_amount = 0
            new_mana_points = 0
            if mana + amount_mp > Heroes.MAX_MP:
                rest_amount = (mana + amount_mp) - Heroes.MAX_MP
                new_mana_points = Heroes.MAX_MP
            else:
                new_mana_points = mana + amount_mp
            self.heroes[hero_name] = {}
            self.heroes[hero_name][hp] = new_mana_points
            print(f"{hero_name} recharged for {amount_mp - rest_amount} MP!")

    def heal(self, hero_name, amount_hp):
        for hp, mana in self.heroes[hero_name].items():
            rest_amount = 0
            new_hp_points = 0
            if hp + amount_hp > Heroes.MAX_HP:
                rest_amount = (hp + amount_hp) - Heroes.MAX_HP
                new_hp_points = Heroes.MAX_HP
            else:
                new_hp_points = hp + amount_hp
            self.heroes[hero_name] = {}
            self.heroes[hero_name][new_hp_points] = mana
            print(f"{hero_name} healed for {amount_hp - rest_amount} HP!")

    def playing_game(self):
        command = input()

        while command != "End":
            command = command.split(" - ")

            if command[0] == "CastSpell":
                self.castspell(command[1], int(command[2]), command[3])
            elif command[0] == "TakeDamage":
                self.takedamage(command[1], int(command[2]), command[3])
            elif command[0] == "Recharge":
                self.recharge(command[1], int(command[2]))
            elif command[0] == "Heal":
                self.heal(command[1], int(command[2]))

            command = input()

    def __repr__(self):
        result = []
        for hero in self.heroes.keys():
            result.append(hero)
            for hp, mp in self.heroes[hero].items():
                result.append(f"  HP: {hp}")
                result.append(f"  MP: {mp}")
        return '\n'.join(result)


heroes_game = Heroes(int(input()))
heroes_game.fill_the_heroes()
heroes_game.playing_game()
print(heroes_game)
