def check_spell(spell, spell_dict):
    points = 0

    for subspell in spell_dict:

        how_many = spell.count(subspell)

        points = points + (how_many * spell_dict[subspell])

        spell = spell.split(subspell)
        spell_parts = ""

        for part in spell:
            spell_parts = spell_parts + part

        spell = spell_parts

    points = points - len(spell)

    return points
        
def swich_dict(spell_dict):

    first_spell = list(spell_dict)[0]
    first_value = spell_dict[first_spell]

    del spell_dict[first_spell]

    spell_dict[first_spell] = first_value

    print(spell_dict)
    return spell_dict
        
def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """

    subspells_dict = {'dai':5, 'ain':3, 'jee':3, 'je': 2, 'ne':2, 'ai':2, 'fe': 1}
    points = []

    start = spell.find('fe')
    end = spell.rfind('ai')

    # if spell is incorect return 0

    if end < start or start == -1 or end == -1:
        return 0

    # cut unnecessary letters
    spell = spell[start:(end+2)]
    subspells_dict_lenght = len(subspells_dict)

    for i in range(subspells_dict_lenght):

        points.append(0)

        points[i] = check_spell(spell, subspells_dict)

        if points[i] < 0:
            points[i] = 0

        swich_dict(subspells_dict)

    print(points)
    points = max(points)

    return(points)


spell = input('Please get a spell: ')

# spell = 'feaineain'

print(damage(spell))