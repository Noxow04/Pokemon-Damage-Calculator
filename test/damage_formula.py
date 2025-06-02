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