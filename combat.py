import random

def dmg_calc(strength):   
    str_stat = strength
    modifiers = [1.5, 2, 2.5]
    str_mod = float("".join(map(str, random.choices(modifiers, weights=[15, 60, 25], k = 1))))
    base_damage = float(str_stat * str_mod)
    return round(base_damage)

    #enemy_choice = random.choices(enemy_id, weights=[30, 20, 10, 5, 0, 2], k = 1)
def enemy_dmg_calc(x):
    if x == [1]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = int(random.choice("12345"))
            print(f"* Goblin claws at you. {e_damage} damage inflicted. *")
        elif move == 2:
            e_damage = int(random.choice("34567"))
            print(f"* Goblin uses Goblin Punch! {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = 0
            print(f"* Goblin is glaring at you. *")
    if x == [2]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = int(random.choice("12345"))
            print(f"* Cockatrice claws at you. {e_damage} damage inflicted. *")
        elif move == 2:
            e_damage = int(random.choice("45678"))
            print(f"* Cockatrice casts Aero. {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = int(random.choice("234")) * 2
            print(f"* Cockatrice jumps up and stomps on you. {e_damage} damage inflicted. *")
    if x == [3]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = int(random.choice("23456"))
            print(f"* Hellhound bites at you. {e_damage} damage inflicted. *")
        elif move == 2:
            e_damage = int(random.choice("56789"))
            print(f"* Hellhound casts Fire. {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = int(random.choice("345")) * 2
            print(f"* Hellhound unleashes a sonic howl. {e_damage} damage inflicted. *")
    if x == [4]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = int(random.choice("567"))
            print(f"* Undead Knight slashes at you. {e_damage} damage inflicted. *")
        elif move == 2:
            e_damage = int(int(random.choice("68")) * 1.5)
            print(f"* Undead Knight casts Dark! {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = 10
            print(f"* Undead Knight bashes you with its shield. {e_damage} damage inflicted. *")
    if x == [5]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = int(random.choice("678"))
            print(f"* Lich King releases a miasma. {e_damage} damage inflicted. *")
        elif move == 2:
            e_damage = int(random.choice("68")) * 2
            print(f"* Lich King casts Shadow Slash! {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = 10 * int(random.choice("123"))
            print(f"* Lich King casts Shadow Flare!. {e_damage} damage inflicted. *")
    if x == [6]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = 0
            print(f"** Sparkle is dazzling! **")
        elif move == 2:
            e_damage = 1
            print(f"* Sparkle zaps you. {e_damage} damage inflicted. *")
        elif move == 3:
            e_damage = 10
            print(f"* Sparkle glows radiantly and bursts. {e_damage} damage inflicted. *")
    if x == [7]:
        move = int(random.choice("123"))
        if move == 1:
            e_damage = 0
            print(f"** Rhobunny is grazing! **")
        elif move == 2:
            e_damage = -10
            print(f"* Rhobunny casts a heal on you. 10 HP recovered. *")
        elif move == 3:
            e_damage = 10
            print(f"* Rhobunny bites gently. 10 damage inflicted. *")
    return e_damage

# def cast_spell(spell, magic):
#     spell_damage = 0
#     if spell == 1:
#         #fireball
#         spell_damage = magic * int(random.choice("345"))
#         print(f"= You blasted the enemy with fire. {spell_damage} damage dealt. =")
#         return spell_damage
#     elif spell == 2:
#         #healing
#         spell_damage = (magic * int(random.choice("456"))) + magic
#         print(f"= You cast a healing spell. {spell_damage} HP recovered. =")
#         return spell_damage
    

    