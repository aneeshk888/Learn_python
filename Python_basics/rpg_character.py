def create_character(name, strength, intelligence, charisma):
    # --- Name validation ---
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    # --- Stats validation ---
    stats = [strength, intelligence, charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    # --- Helper to build stat line ---
    def stat_line(label, value):
        return f"{label} {'●' * value}{'○' * (10 - value)}"
    
    # --- Output ---
    return f"{name}\n{stat_line('STR', strength)}\n{stat_line('INT', intelligence)}\n{stat_line('CHA', charisma)}"


# ✅ Example test
print(create_character('ren', 4, 2, 1))
