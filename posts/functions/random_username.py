import random

def get_random_username():
    prefix = [
        "Dark", "Silent", "Toxic", "Hyper", "Shadow", "Frost", "Iron", "Blazing", "Savage", "Neon",
        "Crimson", "Venom", "Cyber", "Omega", "Void", "Steel", "Chaos", "Blood", "Grim", "Turbo",
        "Death", "Night", "Inferno", "Rogue", "Storm", "Ultra", "Wicked", "Zero", "Blaze", "Ghost"
    ]
    middle = [
        "Wolf", "Blade", "Skull", "Viper", "Storm", "Ghost", "Reaper", "Hawk", "Phantom", "Demon",
        "Knight", "Raven", "Dragon", "Sniper", "Titan", "Cobra", "Specter", "Wraith", "Striker", "Hunter",
        "Banshee", "Predator", "Ronin", "Jackal", "Phoenix", "Slayer", "Golem", "Lynx", "Tempest", "Shade"
    ]
    sufix = [
        "360", "X", "Pro", "HD", "99", "Xx", "II", "Zz", "666", "Elite",
        "V2", "Max", "Ultra", "OG", "420", "Zero", "Alpha", "Omega", "4K", "EXE",
        "OP", "XD", "777", "God", "Senpai", "NoScope", "1337", "AFK", "GG", "Boss"
    ]
    return f"{prefix[random.randrange(0, len(prefix) - 1)]}{middle[random.randrange(0, len(middle) - 1)]}{sufix[random.randrange(0, len(sufix) - 1)]}"
