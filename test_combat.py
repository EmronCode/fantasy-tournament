from characters import Character
from combat import get_moves, determine_target, select_move, take_action, determine_character_list
from match import quick_add_team_member

Jinxx = Character("Jinxx", "Mage", 75, 15, 31, 10, 15, 10, "Light", "Dark")
Peachy = Character("Peachy", "Mage", 75, 18, 25, 10, 15, 11, "Fire", "Light")
Gold = Character("Gold", "Mage", 93, 15, 25, 10, 12, 12, "Water", "Air")
Night = Character("Night", "Rogue", 100, 20, 25, 10, 7, 16, "Earth", "Air")
Shortie = Character("Shortie", "Mage", 75, 15, 25, 12, 15, 9, "Earth", "Light")
Sun = Character("Sun", "Warrior", 125, 31, 15, 12, 10, 5, "Fire", "Water")
Moon = Character("Moon", "Cleric", 75, 1, 1, 18, 18, 7, "Earth", "Light")
Lotus = Character("Lotus", "Rogue", 125, 20, 25, 10, 7, 12, "Water", "Earth")
Stone = Character("Stone", "Rogue", 125, 20, 31, 7, 7, 14, "Water", "Dark")
Goat = Character("Goat", "Archer", 125, 31, 20, 7, 10, 2, "Fire", "Air")
Fury = Character("Fury", "Archer", 125, 25, 20, 10, 12, 1, "Earth", "Light")
Ghost = Character("Ghost", "Rogue", 100, 20, 31, 7, 7, 15, "Air", "Dark")
Beastie = Character("Beastie", "Cleric", 93, 1, 1, 15, 18, 8, "Water", "Light")
Galaxy = Character("Galaxy", "Archer", 125, 25, 25, 7, 10, 3, "Air", "Dark")
Akame = Character("Akame", "Warrior", 100, 31, 20, 12, 10, 6, "Fire", "Dark")
Emron = Character("Emron", "Warrior", 100, 31, 15, 15, 10, 4, "Fire", "Earth")

debug_team = [Emron, Jinxx, Lotus, Goat]

LavaBolt = [Gold, Akame, Emron, Jinxx]
SpaceRock = [Shortie, Sun, Night, Moon]
FrostHammer = [Ghost, Lotus, Fury, Galaxy]
JungleTorch = [Goat, Stone, Beastie, Peachy]

# Test get_moves()
print(get_moves(Emron))
print(get_moves(Galaxy))
print(get_moves(Beastie))

print(" ")

# Test determine_target()
print(determine_target(debug_team, Emron))
print(determine_target(debug_team, Galaxy))
print(determine_target(debug_team, Beastie))

print(" ")

# Test select_move()
print(select_move(Emron, Sun)) # Class = Warrior, thus Physical
print(select_move(Jinxx, Night)) # Class = Mage, thus Magical
print(select_move(Night, Gold)) # STR = 20, MG_PW = 25, thus Magical
print(select_move(Goat, Peachy)) # STR = 31, MG_PW = 20, thus Physical
print(select_move(Beastie, Stone)) # Class = Cleric, thus Heal

print(" ")

# Test take_action()
# Before Team Health
print(str(Gold) + ' ' + str(Gold.health) + '/' + str(Gold.max_health))
print(str(Jinxx) + ' ' + str(Jinxx.health) + '/' + str(Jinxx.max_health))
print(str(Shortie) + ' ' + str(Shortie.health) + '/' + str(Shortie.max_health))

# Night takes action and attacks
take_action([Jinxx, Gold, Shortie], Night)
print("Night Attacks!")

# After Team Health
print(str(Gold) + ' ' + str(Gold.health) + '/' + str(Gold.max_health))
print(str(Jinxx) + ' ' + str(Jinxx.health) + '/' + str(Jinxx.max_health))
print(str(Shortie) + ' ' + str(Shortie.health) + '/' + str(Shortie.max_health))


# Test determine_character_lists
quick_add_team_member(LavaBolt)
quick_add_team_member(SpaceRock)

print(determine_character_list(LavaBolt, SpaceRock, Emron))
print(determine_character_list(LavaBolt, SpaceRock, Night))

# Check if Cleric works as intended
print(determine_character_list(LavaBolt, SpaceRock, Moon)) # No one is hurt, thus return LavaBolt
take_action([Shortie], Gold)
print(determine_character_list(LavaBolt, SpaceRock, Moon)) # Shortie is hurt, thus return Moon's team members
