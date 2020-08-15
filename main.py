import random

DISTINCT_UNITS = False
DISTINCT_HEROES = True
DISTINCT_CLASS = True

### Earth Class ###
class Earth:
    Characters = ['Anwen', 'Findan']
    Units = ['Hunter', 'Pixie', 'Bear']
    Heroes = ['Druid', 'Deer', 'Unicorn']
    Elite = ['Emerald Dragon', 'Treant']
    Artifacts = [
                'Leaf Plate',
                ['Dragon Scales', 'Emerald Dragon'],
                ['Deer Antler', 'Deer'],
                'Doubling Cape',
                ['Elder Staff', 'Druid'],
                'Ring of Life',
                'Boost Boots'
            ]

### Lightning Class ###
class Lightning:
    Characters = ['Nadia', 'Cyrus', 'Azh Rafir']
    Units = ['Apprentice', 'Gremlin', 'Golem']
    Heroes = ['Mage', 'Djinn']
    Elite = ['Phoenix', 'Titan', 'Rakshasa']
    Artifacts = [
                'Gauntlet',
                'Absorb Circlet',
                ['Djinn\'s Sash', 'Djinn'],
                'Battle Wand',
                ['Scimitar', 'Rakshasa'],
                ['Golden Fist', 'Titan'],
                'Mana Shield'
            ]


### Light Magic Class ###
class Light_Magic:
    Characters = ['Godric', 'Varkas', 'Carlyle']
    Units = ['Swordsman', 'Spearman', 'Archer']
    Heroes = ['Knight', 'Priestess']
    Elite = ['Angel', 'Griffin', 'Sword Master']
    Artifacts = [
                'King\'s Crown',
                ['Blessed Wing', 'Angel'],
                'Holy Blade',
                ['Knight\'s Armor', 'Knight']
            ]

### Dark Magic Class ###
class Dark_Magic:
    Characters = ['Fiona', 'Markal', 'Ludmilla']
    Units = ['Skeleton', 'Zombie', 'Ebon Guard']
    Heroes = ['Vampire', 'Ghost']
    Elite = ['Bone Dragon', 'Death Knight', 'Wraith']
    Artifacts = [
                'Blood Ring',
                'Twilight Urn',
                'Cursed Shield',
                ['Blood of the One', 'Vampire'],
                ['Talon\'s Talon', 'Bone Dragon'],
                'Crown of Thorns',
                'Spider Cloak',
                ['Plague Rat', 'Zombie']
            ]

# Fire class
class Fire:
    Characters = ['Aidan', 'Jezebeth', 'Azexes']
    Units = ['Imp', 'Horned Demon', 'Hellhound']
    Heroes = ['Nightmare', 'Succubus']
    Elite = ['Abyssal Lord', 'Pit Fiend', 'Sorcerer']
    Artifacts = [
                'Rage Shield',
                ['Burning Horn', 'Succubus'],
                [ 'Pit master\'s Tail', 'Pit Fiend' ],
                'Celerity Ring',
                'Volcano Armor',
                'Crippling Flail',
                'Thorn Whip',
                'Revive Flame',
                'Magma Shard'
            ]




# Return random Character, Units, Heroes, and Artifact
def rand_class(character_class):

    # Random character
    rand_character = random.choice(character_class.Characters)

    # Three random units
    rand_units = []
    u = 3
    while(u>0):
        if not DISTINCT_UNITS:
            rand_units.append(random.choice(character_class.Units))
            u -= 1
        else:
            rand_units = character_class.Units
            u = 0

    # One random hero & one random elite
    rand_heroes = []
    rand_heroes.append(random.choice(character_class.Heroes))
    rand_elite = []
    rand_elite.append(random.choice(character_class.Elite))

    # One random artifact
    # If the artifact has character mappings,
    # check to make sure it's mappings include
    # the current unit list or hero list
    rand_artifact = random.choice(character_class.Artifacts)
    check = True
    while check:
        if not isinstance(rand_artifact, str):
            match_units = all(item in rand_units for item in rand_artifact)
            match_heroes = all(item in rand_heroes for item in rand_artifact)
            match_elite = all(item in rand_elite for item in rand_artifact)
            if not match_units and not match_heroes and not match_elite:
                rand_artifact = random.choice(character_class.Artifacts)
            else:
                check = False
                rand_artifact = rand_artifact[0]
        else:
            check = False


    # Create and return Class dict
    class_dict = {
                    "Character" : str(rand_character),
                    "Units": list(rand_units),
                    "Heroes" : list(rand_heroes),
                    "Elite" : list(rand_elite),
                    "Artifact" : str(rand_artifact)
                }
    return class_dict


if __name__ == '__main__':
    # Available game classes
    game_classes = ['Fire', 'Light_Magic', 'Dark_Magic', 'Earth', 'Lightning']

    # Pick a class and randomize it for Player 1
    my_new_class = random.choice(game_classes)
    #print(my_new_class)
    my_new_class_dict = rand_class(eval(my_new_class))

    # Output Player One's selection
    print("################")
    print("#  Player One  #")
    print("################")
    print(my_new_class)
    print('Character:')
    print("    " + my_new_class_dict['Character'])
    print("Units: ")
    for unit in my_new_class_dict['Units']:
        print("    " + unit)
    print("Hero:")
    for hero in my_new_class_dict['Heroes']:
        print("    " + hero)
    print("Elite:")
    for elite in my_new_class_dict['Elite']:
        print("    " + elite)
    print('Artifact:')
    print("    " + my_new_class_dict['Artifact'])

    # Create white space
    print('\n\n')

    # Pick a class and randomize it for PLayer 2
    my_new_class_2 = random.choice(game_classes)
    if DISTINCT_CLASS:
        while str(my_new_class_2) == str(my_new_class):
            #print("Player1: " + my_new_class)
            #print("Player2: " + my_new_class_2)
            my_new_class_2 = random.choice(game_classes)
    my_new_class_dict_2 = rand_class(eval(my_new_class_2))

    # Output Player Two's selection
    print("################")
    print("#  Player Two  #")
    print("################")
    print(my_new_class_2)
    print('Character:')
    print("    " + my_new_class_dict_2['Character'])
    print("Units: ")
    for unit in my_new_class_dict_2['Units']:
        print("    " + unit)
    print("Hero:")
    for hero in my_new_class_dict_2['Heroes']:
        print("    " + hero)
    print("Elite:")
    for elite in my_new_class_dict_2['Elite']:
        print("    " + elite)
    print('Artifact:')
    print("    " + my_new_class_dict_2['Artifact'])
