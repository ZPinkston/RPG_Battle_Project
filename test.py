import random
import sys
from combat import *
from enemies import *
from leveling import *

def combat_init():
    total_experience = 0
    battle_count = 0
    while True:
        victory_statement = "The enemy perished. You won!"
        in_combat = True
        while in_combat == True:
            enemy_id = [1, 2, 3, 4, 5, 6]
            if battle_count < 10:
                enemy_choice = random.choices(enemy_id, weights=[30, 20, 10, 5, 0, 2], k = 1)
            elif battle_count >= 10 and battle_count < 20:
                enemy_choice = random.choices(enemy_id, weights=[20, 20, 20, 15, 1, 2], k = 1)
            elif battle_count >= 20 and battle_count < 30:
                enemy_choice = random.choices(enemy_id, weights=[1, 10, 10, 20, 2, 1], k = 1)
            elif battle_count >= 30:
                enemy_choice = random.choices(enemy_id, weights=[0, 1, 1, 5, 10, 5], k = 1)
            
            enemy_hp, enemy_message, exp_given = enemy_selector(enemy_choice)
            max_hp, max_mp, current_level, strength, magic = level_up(total_experience)
            print(f"Current level: {current_level}\nHP = {max_hp}\nMP = {max_mp}\nStrength = {strength}\nMagic = {magic}\nBattle count = {battle_count}\n\n")
            print(f"Enemy has appeared.")
            print(enemy_message)
            current_hp = max_hp
            current_mp = max_mp
            buff_spell_count = 0
            barrier_spell_count = 0
            while enemy_hp > 0 and current_hp > 0 and in_combat == True:
                if barrier_spell_count > 2:
                    barrier_spell_count = 2
                if buff_spell_count > 3:
                    buff_spell_count = 3
                print(" ")
                if in_combat == True and current_hp > 0:
                    try: 
                        actions = (1,2,3,4)
                        action_input = int(input("= Select 1 to attack, 2 for magic, 3 to defend, or 4 to run: "))
                        if action_input in actions:
                            action = action_input
                        else:
                            raise ValueError
                        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
                        if buff_spell_count > 0:
                            buff_spell_count -= 1
                        if barrier_spell_count > 0:
                            barrier_spell_count -= 1
                        print(" ")
                        if action == 1:
                            print("===== You attack! =====")
                            damage = dmg_calc(strength)
                            if buff_spell_count >= 1:
                                enemy_hp = enemy_hp - (damage * 2)
                                print(f"= {damage * 2} damage inflicted. =\n")
                            else:
                                enemy_hp = enemy_hp - damage
                                print(f"= {damage} damage inflicted. =\n")
                            
                        elif action == 2:
                            try:
                                spells = (1, 2, 3, 4)
                                spell_input = int(input(f"== Magic: 1: Fireball, 2: Heal, 3: Barrier, 4: Boost : "))
                                if spell_input in spells:
                                    spell = spell_input
                                else:
                                    raise ValueError
                                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
                                print(" ")
                                if spell == 1 and current_mp >= 2:
                                    enemy_hp = enemy_hp - cast_spell(spell, magic)
                                    current_mp -= 2
                                elif spell == 2 and current_mp >= 2:
                                    current_hp = current_hp + cast_spell(spell, magic)
                                    current_mp -= 2
                                    if current_hp > max_hp:
                                        current_hp = max_hp
                                elif spell == 3 and current_mp >= 5:
                                    barrier_spell_count += 2
                                    current_mp -= 5
                                    print("= You cast a protective barrier. (2 charges) =")
                                elif spell == 4 and current_mp >= 4:
                                    buff_spell_count = 3
                                    current_mp -= 4
                                    print("= You boost your offensive power. (3 charges) =")
                                else:
                                    print(f"= Insufficient MP. The spell failed.= ")
                            except ValueError:
                                print("== Spell failed! ==")

                        elif action == 3:
                            current_hp += int((0.25 * max_hp) + current_level)
                            current_mp += int(0.2 * max_mp)
                            print(f"= You defend and recover HP and MP.= ")
                            if current_hp > max_hp:
                                current_hp = max_hp
                            if current_mp > max_mp:
                                current_mp = max_mp
                            
                        elif action == 4:
                            print("== You run away. ==")
                            in_combat = False
                    except ValueError:
                        print("Please enter 1, 2, 3, or 4.")

                    #enemy damage calc
                    if barrier_spell_count >= 1:
                        print("* Enemy attacks. Your barrier negates the damage. *")
                    elif enemy_hp > 0 and in_combat == True:
                        current_hp = current_hp - enemy_dmg_calc(enemy_choice)

                    if current_hp <= 0:
                        print(f"=== You were defeated. ===")
                        in_combat = False
                        break
                    elif enemy_hp <= 0:
                        total_experience = total_experience + exp_given
                        if exp_given == 500:
                            print("The Lich King has been defeated. You saved the world!")
                            in_combat = False
                            break
                        else:
                            print(victory_statement)
                            print(f"= You gained {exp_given} experience. =")
                            battle_count += 1

                    elif in_combat == True:
                        print(f"\n{current_hp} HP remaining. {current_mp} MP remaining")
                        print(f"Buffs: {buff_spell_count}; Barriers: {barrier_spell_count}")
                        print(f"Enemy HP: {enemy_hp}")
                        
                elif in_combat == True:
                    continue    
                    
            else:
                break
            continue_question = input("Input anything to continue, or 'exit' to quit: ")
            if continue_question.lower() == "exit":
                in_combat = False
                print("End program.")
                sys.exit()
            else:
                combat_init()

combat_init()
