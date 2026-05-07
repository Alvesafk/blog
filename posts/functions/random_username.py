import random

def get_random_username():
    prefix = [
        "Dark",
        "Silent",
        "Toxic",
        "Hyper",
        "Shadow",
        "Frost",
        "Iron",
        "Blazing",
        "Savage",
        "Neon"
    ] 

    middle = [
        "Wolf",
        "Blade",
        "Skull",
        "Viper",
        "Storm",
        "Ghost",
        "Reaper",
        "Hawk",
        "Phantom",
        "Demon",
    ]

    sufix = [
        "360",
        "X",
        "Pro",
        "HD",
        "99",
        "Xx",
        "II",
        "Zz",
        "666",
        "Elite",
    ]
    return f"{prefix[random.randrange(0, len(prefix) - 1)]}{middle[random.randrange(0, len(middle) - 1)]}{sufix[random.randrange(0, len(sufix) - 1)]}"
