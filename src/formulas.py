from packages import *

from damage_factors import DamageFactors
from extra_factors import ExtraFactors

import utils


def stat_formula(base, iv, ev, nature, level=100):
    """
    :param base: int in 5-255
    :param iv: int in 0-31
    :param ev: int in 0-252
    :param nature: .9, 1 or 1.1
    :param level: int in 1-100
    """
    return floor(floor((2 * base + iv + floor(ev / 4)) * level / 100) + 5 * nature)


def hp_formula(base, iv, ev, level=100):
    """
    :param base: int in 5-255
    :param iv: int in 0-31
    :param ev: int in 0-252
    :param level: int in 1-100
    """
    return floor((2 * base + iv + floor(ev / 4)) * level / 100) + level + 10


def damage_formula(level, power, attack, defense, other_factors: DamageFactors):
    result = floor(((((2 * level) / 5 + 2) * power * (attack / defense)) / 50) + 2)
    factors = other_factors.variables
    count = 0
    for factor in factors:
        assert(factor)
        if count in (4, 6):
            #random or type_effectiveness
            result = floor(result * factor)
        else:
            result = utils.my_round_down(result * factor)
        count += 1
    return result
    

def attack_range(factors: DamageFactors, level, power, attack, defense):
    factors.random = .85
    min_damage = damage_formula(level, power, attack, defense, factors)
    factors.random = 1
    max_damage = damage_formula(level, power, attack, defense, factors)
    return min_damage, max_damage


def main():
    ic('testing :')
    # abomasnow on abomasnow blizzard test
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 1,
        "type_effectiveness": 0,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": False,
            "expert_belt": False,
            "life_orb": False,
            "metronome": False
        })})
    returned = attack_range(damage_factors_test_values, 100, 110, stat_formula(92, 31, 0, 1, 100),
                          stat_formula(85, 31, 0, 1, 100))
    expected = (127, 150)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # abomasnow on abomasnow earth power life orb on light screen test
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 0,
        "type_effectiveness": -1,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": True,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": False,
            "expert_belt": False,
            "life_orb": True,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 100, 90, stat_formula(92, 31, 0, 1, 100),
                          stat_formula(85, 31, 0, 1, 100))
    expected = (22, 27)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # lvl 75 glaceon ice fang on grachomp (bulbapedia example 1)
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 1,
        "type_effectiveness": 2,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": False,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 75, 65, 123, 163)
    expected = (168, 196)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # lvl 75 glaceon muscle band ice fang crtical on grachomp (bulbapedia example 2)
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": True,
        "random": None,
        "stab": 1,
        "type_effectiveness": 2,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": 0,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 75, 71, 123, 163)
    expected = (268, 324)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # burned kartana giga impact on arceus fighting
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 0,
        "type_effectiveness": 0,
        "burn": True,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": 0,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 100, 150, 507, 372)
    expected = (73, 86)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    #groudon earthquake expert belt on Heatran
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 1,
        "type_effectiveness": 2,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": 0,
            "expert_belt": True,
            "life_orb": False,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 100, 100, 438, 311)
    expected = (734, 864)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    #yanmega tinted lens surf under the rain on amoonguss
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 1,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 0,
        "type_effectiveness": -1,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": True,
            "fluffy": False,
            "type_berry": 0,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 100, 90, 364, 284)
    expected = (124, 146)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    #cryogonal adaptability life orb ice beam on yache berry garchomp
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 2,
        "type_effectiveness": 2,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": False,
            "type_berry": 1,
            "expert_belt": False,
            "life_orb": True,
            "metronome": 0
        })})
    returned = attack_range(damage_factors_test_values, 100, 90, 226, 206)
    expected = (369, 437)
    if returned[0] == expected[0] and returned[1] == expected[1]:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    #volcarona tera fire adaptability fireblast metronome after 2 uses under the rain on fluffy blissey
    damage_factors_test_values = DamageFactors.quick_setup({
        "pb": False,
        "weather": -1,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 3,
        "type_effectiveness": 0,
        "burn": False,
        "zmove": False,
        "other": ExtraFactors.quick_setup({
            "dynamax": False,
            "minimize": False,
            "dig_dive": False,
            "screens": False,
            "paradox_duo_attack": False,
            "multiscale_and_others": False,
            "filter_and_others": False,
            "neuroforce": False,
            "sniper": False,
            "tinted_lens": False,
            "fluffy": True,
            "type_berry": 0,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 2
        })})
    returned = attack_range(damage_factors_test_values, 100, 110, 306, 306)
    expected = (246, 297)
    if returned == expected:
        ic("ok")
    else:
        ic(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

if __name__ == "__main__":
    ic.configureOutput(prefix="> ")
    main()
