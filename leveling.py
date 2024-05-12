def level_up(x):
    current_xp = x
    current_level = 1
    if current_xp < 20:
        max_hp = 20
        max_mp = 10 
        current_level = 1
        strength = 2
        magic = 2
    
    elif current_xp >= 20 and current_xp < 50:
        max_hp = 22
        max_mp = 11
        current_level = 2
        strength = 3
        magic = 2
    
    elif current_xp >= 50 and current_xp < 100:
        max_hp = 25
        max_mp = 12
        current_level = 3
        strength = 3
        magic = 3

    elif current_xp >= 100 and current_xp < 175:
        max_hp = 28
        max_mp = 14
        current_level = 4
        strength = 4
        magic = 3
    
    elif current_xp >= 175 and current_xp < 275:
        max_hp = 30
        max_mp = 15
        current_level = 5
        strength = 4
        magic = 4

    elif current_xp >= 275 and current_xp < 400:
        max_hp = 34
        max_mp = 17
        current_level = 6
        strength = 5
        magic = 4
    
    elif current_xp >= 400 and current_xp < 550:
        max_hp = 38
        max_mp = 19
        current_level = 7
        strength = 5
        magic = 5

    elif current_xp >= 550 and current_xp < 725:
        max_hp = 42
        max_mp = 21
        current_level = 8
        strength = 6
        magic = 5

    elif current_xp >= 725 and current_xp < 925:
        max_hp = 46
        max_mp = 23
        current_level = 9
        strength = 6
        magic = 6
    
    elif current_xp >= 925 and current_xp < 1150:
        max_hp = 50
        max_mp = 25
        current_level = 10
        strength = 7
        magic = 6

    elif current_xp >= 1150 and current_xp < 1400:
        max_hp = 56
        max_mp = 28
        current_level = 11
        strength = 7
        magic = 7

    elif current_xp >= 1400 and current_xp < 1675:
        max_hp = 60
        max_mp = 30
        current_level = 12
        strength = 8
        magic = 7

    elif current_xp >= 1675 and current_xp < 1975:
        max_hp = 66
        max_mp = 33
        current_level = 13
        strength = 8
        magic = 8
    
    elif current_xp >= 1975 and current_xp < 2300:
        max_hp = 72
        max_mp = 36
        current_level = 14
        strength = 9
        magic = 8

    elif current_xp >= 2300 and current_xp < 2650:
        max_hp = 78
        max_mp = 39
        current_level = 15
        strength = 9
        magic = 9

    elif current_xp >= 2650 and current_xp < 3025:
        max_hp = 84
        max_mp = 42
        current_level = 16
        strength = 10
        magic = 9

    elif current_xp >= 3025 and current_xp < 3425:
        max_hp = 90
        max_mp = 45
        current_level = 17
        strength = 10
        magic = 10

    elif current_xp >= 3425 and current_xp < 3850:
        max_hp = 96
        max_mp = 48
        current_level = 18
        strength = 11
        magic = 10
    
    elif current_xp >= 3850 and current_xp < 4300:
        max_hp = 106
        max_mp = 50
        current_level = 19
        strength = 11
        magic = 11

    elif current_xp >= 4300 and current_xp < 4800:
        max_hp = 120
        max_mp = 50
        current_level = 20
        strength = 12
        magic = 11

    else:
        max_hp = 125
        max_mp = 50
        current_level = 21
        strength = 12
        magic = 12
        print(f"Max level achieved.")

    return max_hp, max_mp, current_level, strength, magic
