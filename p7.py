#p7.py#
#Min Kim#
#CS216#

# Starting character
Norm = {
    "name": "Norm the Forester",
    "health": 100,
    "mana": 50,
    "attack": 20
}

Lara = {
    "name": "Lara the Swift",
    "health": 100,
    "mana": 60,
    "attack": 10    
}

Drax = {
    "name": "Drax the Mighty",
    "health": 100,
    "mana": 30,
    "attack": 25
}

# TODO: Add at least two more attributes to Norm
# (include "attack" for battle)

# TODO: Create two additional characters


def update_health(character, amount):
    # TODO: update health
    # ensure it stays between 0 and 100
    character["health"] += amount
    if character["health"] < 0:
        character["health"] = 0
    elif character["health"] > 100:
        character["health"] = 100


def display_character(character):
    # TODO: print name
    # TODO: print health
    # TODO: print other attributes
    print(f"Name: {character['name']}")
    print(f"Health: {character['health']}")
    for key, value in character.items():
        if key != "name" and key !="health":
            print(f"{key}: {value}")

def attack(attacker, defender):
    # TODO:
    # get attack value
    # reduce defender health using update_health
    # print attack message
    dmg = attacker["attack"]
    update_health(defender, -dmg)
    print(f"{attacker['name']} attacks {defender['name']}!")
    print(f"{defender['name']} loses {dmg} health.\n")
    


# --- User Input for New Attribute ---
# TODO: ask user for attribute name
# TODO: ask user for value
# TODO: add to Norm dictionary
attr_name = input("Enter attribute name: ")
attr_value = input("Enter value: ")
Norm[attr_name] = attr_value

# --- Test your functions ---

update_health(Norm, -20)

# TODO: call attack between two characters
attack(Norm, Lara)
display_character(Norm)
display_character(Lara)
display_character(Drax)

# TODO: display your other two characters