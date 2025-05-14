from characters import Character
from match import play

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

LavaBolt = [Gold, Akame, Emron, Jinxx]
SpaceRock = [Shortie, Sun, Night, Moon]

first_half = [Gold, Akame, Emron, Jinxx, Shortie, Sun, Night, Moon]
second_half = [Ghost, Lotus, Fury, Galaxy, Goat, Stone, Beastie, Peachy]

# Test a "regular" match
play(LavaBolt, SpaceRock)

# Test all 16 Characters
play(first_half, second_half)