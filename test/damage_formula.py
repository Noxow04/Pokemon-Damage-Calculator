import unittest
import sys

sys.path.append("../src")
from formulas import damage_formula, DamageFactors, ExtraFactors

class TestDamageFormula(unittest.TestCase):
    def test_basic_whole_range(self):
        # Test with basic whole range
        # abomasnow on abomasnow blizzard test
        damage_factors_test_values = DamageFactors.from_dict({
            "pb": False,
            "weather": 0,
            "glaiverush": False,
            "critical": False,
            "random": None,
            "stab": 1,
            "type_effectiveness": 0,
            "burn": False,
            "zmove": False,
            "other": ExtraFactors.from_dict({
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
        for random, expected in zip(range(85, 101), (127, 129, 130, 132, 133, 135, 136, 138, 139, 141, 142, 144, 145, 147, 148, 150)):
            damage_factors_test_values.random = random / 100
            returned = damage_formula(100, 110, 220, 206, damage_factors_test_values)
            self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()

    # ic('testing :')
    # # abomasnow on abomasnow blizzard test
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 0,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": False,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": False
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 110, stat_formula(92, 31, 0, 1, 100),
    #                       stat_formula(85, 31, 0, 1, 100))
    # expected = (127, 150)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # # abomasnow on abomasnow earth power life orb on light screen test
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 0,
    #     "type_effectiveness": -1,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": True,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": False,
    #         "expert_belt": False,
    #         "life_orb": True,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 90, stat_formula(92, 31, 0, 1, 100),
    #                       stat_formula(85, 31, 0, 1, 100))
    # expected = (22, 27)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # # lvl 75 glaceon ice fang on grachomp (bulbapedia example 1)
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 2,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": False,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 75, 65, 123, 163)
    # expected = (168, 196)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # # lvl 75 glaceon muscle band ice fang crtical on grachomp (bulbapedia example 2)
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": True,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 2,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 75, 71, 123, 163)
    # expected = (268, 324)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # # burned kartana giga impact on arceus fighting
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 0,
    #     "type_effectiveness": 0,
    #     "burn": True,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 150, 507, 372)
    # expected = (73, 86)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #groudon earthquake expert belt on Heatran
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 2,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": True,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 100, 438, 311)
    # expected = (734, 864)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #yanmega tinted lens surf under the rain on amoonguss
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 1,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 0,
    #     "type_effectiveness": -1,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": True,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 90, 364, 284)
    # expected = (124, 146)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #cryogonal adaptability life orb ice beam on yache berry garchomp
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 2,
    #     "type_effectiveness": 2,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 1,
    #         "expert_belt": False,
    #         "life_orb": True,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 90, 226, 206)
    # expected = (369, 437)
    # if returned[0] == expected[0] and returned[1] == expected[1]:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #volcarona tera fire adaptability fireblast metronome after 2 uses under the rain on fluffy blissey
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": -1,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 3,
    #     "type_effectiveness": 0,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": True,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 2
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 110, 306, 306)
    # expected = (246, 297)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #rayquaza dragon breath on chansey
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 0,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 60, stat_formula(150, 31, 252, 1.1, 100), stat_formula(105, 31, 8, 1, 100))
    # expected = (115, 136)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #rayquaza outrage on pidgeotto
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 0,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 120, stat_formula(150, 31, 252, 1, 100), stat_formula(55, 31, 0, 1, 100))
    # expected = (352, 415)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #marowak bonemerang on pikachu
    # # Note: multihits must use their base power and be multiplied after damage calculation (add that to the Attack class))
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 1,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 50, stat_formula(80, 31, 252, 1.1, 100), stat_formula(40, 31, 0, 1, 100))
    # expected = (264, 312)
    # #252+ Atk Marowak Bonemerang (2 hits) vs. 0 HP / 0 Def Pikachu: 528-624 (divided by 2 because multihit)
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #sawk close combat on staraptor
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": 0,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 120, stat_formula(125, 31, 252, 1.1, 100), stat_formula(70, 31, 0, 1, 100))
    # expected = (280, 331)
    # #252+ Atk Sawk Close Combat vs. 0 HP / 0 Def Staraptor: 280-331 (90 - 106.4%) -- 37.5% chance to OHKO
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")

    # #ratata quick attack on onix
    # damage_factors_test_values = DamageFactors.from_dict({
    #     "pb": False,
    #     "weather": 0,
    #     "glaiverush": False,
    #     "critical": False,
    #     "random": None,
    #     "stab": 1,
    #     "type_effectiveness": -1,
    #     "burn": False,
    #     "zmove": False,
    #     "other": ExtraFactors.from_dict({
    #         "dynamax": False,
    #         "minimize": False,
    #         "dig_dive": False,
    #         "screens": False,
    #         "paradox_duo_attack": False,
    #         "multiscale_and_others": False,
    #         "filter_and_others": False,
    #         "neuroforce": False,
    #         "sniper": False,
    #         "tinted_lens": False,
    #         "fluffy": False,
    #         "type_berry": 0,
    #         "expert_belt": False,
    #         "life_orb": False,
    #         "metronome": 0
    #     })})
    # returned = attack_range(damage_factors_test_values, 100, 40, stat_formula(56, 31, 0, 1, 100), stat_formula(160, 31, 0, 1, 100))
    # expected = (9, 11)
    # #0 Atk Rattata Quick Attack vs. 0 HP / 0 Def Onix: 9-11 (4.2 - 5.2%) -- possibly the worst move ever
    # if returned == expected:
    #     ic("ok")
    # else:
    #     print(f"{expected[0]}-{expected[1]} | got {returned[0]}-{returned[1]}")