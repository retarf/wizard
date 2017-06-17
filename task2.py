from itertools import permutations


def get_max_score(spell, spell_dict):

    points = []
    spell_copy = spell

    # use permutation to find every subspell dictionary combination
    for combination in list(permutations(spell_dict)):

        word_points = 0

        for subspell in combination:

            # if subspell is in spellword, add appropriate amount of points
            word_points += (spell.count(subspell) * spell_dict[subspell])

            # delete subspell from spellword
            spell = spell.split(subspell)

            # join spellword parts
            spell_part = ""
            for part in spell:
                spell_part += part

            # new spell, after subspell cuting off
            spell = spell_part

        # Subtract single letters
        word_points -= len(spell)

        # get oryginal spell
        spell = spell_copy
        # add points to
        points.append(word_points)

    score = max(points)

    return score


def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """

    # spells dictionary
    spell_dict = {'dai': 5, 'ain': 3, 'jee': 3,
                  'je': 2, 'ne': 2, 'ai': 2, 'fe': 1}

    # check start and end position
    start = spell.find('fe')
    end = spell.rfind('ai')

    # if spell is incorect return 0
    if end < start or start == -1 or end == -1:
        return 0

    # cut unnecessary letters
    spell = spell[start:(end + 2)]

    # use get_max_score function
    score = get_max_score(spell, spell_dict)

    return score
