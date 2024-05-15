def enemy_selector(x):
    enemy_hp = ""
    enemy_message = ""
    if x == [1]:
        # "Goblin"
        enemy_hp = 20
        enemy_message = "It's a Goblin!"
        exp_given = 10
    elif x == [2]:
        # "Cockatrice"
        enemy_hp = 30
        enemy_message = "Uh oh, a Cockatrice!"
        exp_given = 20
    elif x == [3]:
        # "Hellhound"
        enemy_hp = 40
        enemy_message = "Eek! A Hellhound!"
        exp_given = 30
    elif x == [4]:
        # "Undead Knight"
        enemy_hp = 50
        enemy_message = "It's an Undead Knight!"
        exp_given = 100
    elif x == [5]:
        # "Lich King"
        enemy_hp = 100
        enemy_message = "The Lich King has arisen!"
        exp_given = 500
    elif x == [6]:
        # "Sparkle"
        enemy_hp = 1
        enemy_message = "It is something Sparkle-y..."
        exp_given = 2000
    elif x == [7]:
        # Rhobunny
        enemy_hp = 35
        enemy_message = "It's a cute little Rhobunny!"
        exp_given = (10)
    else:
        print("An ERROR appeared.")
    return enemy_hp, enemy_message, exp_given