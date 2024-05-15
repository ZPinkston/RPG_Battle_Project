import random

def spells(current_level, magic, current_mp):
    spells_known = ["Fireball", "Heal"]
    try:
        if current_level < 5:
            spells_known = spells_known
            print(f"Spells:")
            for i, spell in enumerate(spells_known):
                print(f"{i + 1}: {spell}")
            spell_input = int(input(f"== Cast spell: "))
            
            if 1 <= spell_input <= len(spells_known):
                spell_choice = spells_known[spell_input - 1]
                return cast_spell(spell_choice, magic, current_mp)
            else:
                raise ValueError
        if current_level >= 5 and current_level < 10:
            spells_known = ["Fireball", "Heal", "Barrier"]
            print(f"Spells:")
            for i, spell in enumerate(spells_known):
                print(f"{i + 1}: {spell}")
            spell_input = int(input(f"== Cast spell: "))
            
            if 1 <= spell_input <= len(spells_known):
                spell_choice = spells_known[spell_input - 1]
                print(spell_choice)
                return cast_spell(spell_choice, magic, current_mp)
            else:
                raise ValueError
        if current_level >= 10 and current_level < 15:
            spells_known = ["Fireball", "Heal", "Barrier", "Boost"]
            print(f"Spells:")
            for i, spell in enumerate(spells_known):
                print(f"{i + 1}: {spell}")
            spell_input = int(input(f"== Cast spell: "))
            
            if 1 <= spell_input <= len(spells_known):
                spell_choice = spells_known[spell_input - 1]
                print(spell_choice)
                return cast_spell(spell_choice, magic, current_mp)
            else:
                raise ValueError
        if current_level >= 15:
            spells_known = ["Fireball", "Heal", "Barrier", "Boost", "Lightning"]
            print(f"Spells:")
            for i, spell in enumerate(spells_known):
                print(f"{i + 1}: {spell}")
            spell_input = int(input(f"== Cast spell: "))
            
            if 1 <= spell_input <= len(spells_known):
                spell_choice = spells_known[spell_input - 1]
                print(spell_choice)
                return cast_spell(spell_choice, magic, current_mp)
            else:
                raise ValueError
    except ValueError:
        print("== Spell failed! ==")
        

def cast_spell(spell, magic, current_mp):
    spell_damage = 0
    if spell == "Fireball" and current_mp >= 2:
        #fireball
        spell_damage = magic * int(random.choice("345"))
        print(f"= You blasted the enemy with fire. {spell_damage} damage dealt. =")
        return spell, spell_damage
    
    elif spell == "Heal" and current_mp >= 2:
        #healing
        spell_damage = (magic * int(random.choice("456"))) + magic
        print(f"= You cast a healing spell. {spell_damage} HP recovered. =")
        return spell, spell_damage
    
    elif spell == "Barrier" and current_mp >= 5:
        spell_damage = 0
        print("= You cast a protective barrier. (2 charges) =")
        return spell, spell_damage
    
    elif spell == "Boost" and current_mp >= 5:
        spell_damage = 0
        print("= You boost your offensive power. (3 charges) =")
        return spell, spell_damage
    
    elif spell == "Lightning" and current_mp >= 10:
        spell_damage = magic * int(random.choice("456"))
        print(f"= You unleashed lightning. {spell_damage} damage dealt. =")
        return spell, spell_damage
    
    else:
        print(f"= Insufficient MP. The spell failed. =")

    