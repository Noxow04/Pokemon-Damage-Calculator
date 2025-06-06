from packages import *

from damage_factors import DamageFactors
from extra_factors import ExtraFactors

import utils

STAT_NAMES = ['HP', 'Atk', 'Def', 'SpAtk', 'SpDef', 'Spe']
generic_stats = namedtuple('stats', STAT_NAMES)
# value_id_wrap = namedtuple('value_id_wrap', ['value', 'id'])


def stat_formula(base: int, iv: int, ev: int, nature: float, level: int=100) -> int:
    """
    :param base: base value of the statistic (5-255)
    :param iv: statistic's IVs (0-31)
    :param ev: statistic's EVs (0-252)
    :param nature: effect of the nature on the statistic, negative (.9), neutral (1), or positive (1.1)
    :param level: pokemon level (1-100)
    :return int: computed statistic value
    """
    return floor((floor(((2 * base + iv + floor(ev / 4)) * level) / 100) + 5) * nature)


def hp_formula(base: int, iv: int, ev: int, level:int=100) -> int:
    """
    :param base: base hp statistic (5-255)
    :param iv: hp's IVs (0-31)
    :param ev: hp's EVs (0-252)
    :param level: pokemon level (1-100)
    :return int: computed hp value
    """
    return floor(((2 * base + iv + floor(ev / 4)) * level) / 100) + level + 10

def get_all_stats(bases: generic_stats, ivs: generic_stats, evs: generic_stats, positive_nature: Optional[str], negative_nature: Optional[str], level: int) -> generic_stats:
    """
    :param bases: base statistics
    :param ivs: IV of each statistic
    :param evs: EV of each statistic
    :param positive_nature: name of statistic positively affected by the nature
    :param negative_nature: name of statistic negatively affected by the nature
    :param level: level of the pokemon
    :return generic_stats: returns the calculated stats values as a named tuple
    """
    stats = list()
    nature = 1
    for stat_name in STAT_NAMES:
        if stat_name == 'HP':
            stats.append(hp_formula(bases.HP, ivs.HP, evs.HP, level))
        else:
            nature = 0.9 if stat_name == negative_nature else (1.1 if stat_name == positive_nature else 1)
            stats.append(stat_formula(getattr(bases, stat_name), 
                                      getattr(ivs, stat_name), 
                                      getattr(evs, stat_name), 
                                      nature,
                                      level))
    return generic_stats(*stats)


class Damage:
    def __init__(self) -> None:
        self._level: int = 100
        self._power: Optional[int] = None
        self._attack: Optional[int] = None
        self._defense: Optional[int] = None
        self._other_factors: Optional[DamageFactors] = None

    @property
    def level(self) -> Optional[int]:
        return self._level
    @level.setter
    def level(self, value: int):
        if 1 <= value <= 100:
            self._level = value

    @property
    def power(self) -> Optional[int]:
        return self._power
    @power.setter
    def power(self, value: int):
        if isinstance(value, int) and value > 0:
            self._power = value

    @property
    def attack(self) -> Optional[int]:
        return self._attack
    @attack.setter
    def attack(self, value: int):
        if isinstance(value, int) and value > 0:
            self._attack = value

    @property
    def defense(self) -> Optional[int]:
        return self._defense
    @defense.setter
    def defense(self, value: int):
        if isinstance(value, int) and value > 0:
            self._defense = value

    @property
    def other_factors(self) -> Optional[DamageFactors]:
        return self._other_factors
    @other_factors.setter
    def other_factors(self, value: DamageFactors):
        if isinstance(value, DamageFactors):
            self._other_factors = value

    @property
    def damage(self) -> int:
        """
        :return int: computed damage value
        """
        if not self.level:
            raise ValueError("self.level must not be None for damage calculation")
        if not self.attack:
            raise ValueError("self.attack must not be None for damage calculation")
        if not self.defense:
            raise ValueError("self.defense must not be None for damage calculation")
        if not self.other_factors:
            raise ValueError("self.other_factors must not be None for damage calculation")
        if not self.power:
            raise ValueError("self.power must not be None for damage calculation")
        result = floor(((((2 * self.level) / 5 + 2) * self.power * (self.attack / self.defense)) / 50) + 2)
        factors = self.other_factors.variables
        count = 0
        for factor in factors:
            assert(factor)
            if count in (4, 6):
                #random and type_effectiveness
                result = floor(result * factor)
            else:
                result = utils.my_round_down(result * factor)
            count += 1
        return result

    @property
    def damage_range(self) -> tuple[int, int]:
        """
        :return tuple: minimum and maximum damage values possible
        """
        if not self.other_factors:
            raise ValueError("self.other_factors must not be None for damage calculation")
        self.other_factors.random = .85
        min_damage = self.damage
        self.other_factors.random = 1
        max_damage = self.damage
        return (min_damage, max_damage)

    @property
    def damage_array(self) -> tuple[int, ...]:
        """
        :return tuple: array of all 15 damage values possible
        """
        if not self.other_factors:
            raise ValueError("self.other_factors must not be None for damage calculation")
        damage_values = list()
        for random in range(85, 101):
            self.other_factors.random = random/100
            damage_values.append(self.damage)
        return tuple(damage_values)

    @staticmethod
    def from_dict(dictionary):
        new_instance = Damage()
        for key, value in dictionary.items():
            setattr(new_instance, key, value)
        return new_instance


def main():
    # calculating a lvl 16 / 12 IVs / 0 EVs / neutral nature pidgeotto attack
    pidgeotto_attack = stat_formula(60,    # https://bulbapedia.bulbagarden.net/wiki/Pidgeotto_(Pokémon)#Base_stats
                 12, 0, 1, 16)
    print(f"{pidgeotto_attack = }")

    # calculating a lvl 16 / 12 IVs / 0 EVs / pidgeotto hp
    pidgeotto_hp = hp_formula(63,    # https://bulbapedia.bulbagarden.net/wiki/Pidgeotto_(Pokémon)#Base_stats
                 12, 0, 16)
    print(f"{pidgeotto_hp = }")
    
    # calculating all the stats of a lvl 100 pidgeot
    # with 31 IVs in all stats, 252 EVs in Attack and Speed, 4 EVs in HP
    # and a Jolly nature (+Spe / -SpAtk)
    pidgeot_stats = get_all_stats(generic_stats(83, 80, 75, 70, 70, 101),   # https://bulbapedia.bulbagarden.net/wiki/Pidgeot_(Pokémon)#Generation_VI_onward
                                  generic_stats(31, 31, 31, 31, 31, 31), 
                                  generic_stats(4, 252, 0, 0, 0, 252), 
                                  'Spe', 'SpAtk', 100)
    print(pidgeot_stats)

    # lvl 75 Atk glaceon ice fang on garchomp (bulbapedia example 1 : https://bulbapedia.bulbagarden.net/wiki/Damage#Example)
    damage_factors_test_values = DamageFactors.from_dict({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 1,                  # glaceon is ice-type and so is ice fang
        "type_effectiveness": 2,    # an ice move is 4 times effective on garchomp
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
            "metronome": 0
        })})
    example_1 = Damage.from_dict({
        "level": 75,     # Glaceon level
        "power": 65,     # Base Power (BP) of Ice Fang 
        "attack": 123,    # attack value of the glaceon
        "defense": 163,    # defense value of the garchomp
        "other_factors": damage_factors_test_values
        })
    print(example_1.damage_range) # expected 168-196

    # burned 252 Atk EVs / 31 Atk IVs / positive nature / lvl 100 kartana giga impact
    # on 252 Def Evs / 31 Def IVs / neutral nature / lvl 100 arceus fighting
    kartana_attack = stat_formula(181,  # https://bulbapedia.bulbagarden.net/wiki/Kartana_(Pokémon)#Base_stats
                                  31,   # IVs
                                  252,  # EVs
                                  1.1)  # positive nature
    # since level is 100 by default no need to specify a value
    arceus_defense = stat_formula(120,  # https://bulbapedia.bulbagarden.net/wiki/Arceus_(Pokémon)#Base_stats
                                  31, 252, 1)
    damage_factors_test_values = DamageFactors.from_dict({
        "pb": False,
        "weather": 0,
        "glaiverush": False,
        "critical": False,
        "random": None,
        "stab": 0,                  # kartana is not normal-type and giga impact is a normal attack
        "type_effectiveness": 0,    # a normal attack has neutral effectiveness on Arceus-fighting
        "burn": True,               # as stated, kartana is burned
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
            "type_berry": 0,
            "expert_belt": False,
            "life_orb": False,
            "metronome": 0
        })})
    example_2 = Damage.from_dict({
        "level": 100,    # kartana level 
        "power": 150,    # giga impact BP
        "attack": kartana_attack, 
        "defense": arceus_defense, 
        "other_factors": damage_factors_test_values
        })
    print(example_2.damage_range)
    # expected 80-95 from https://calc.pokemonshowdown.com :     
    # 252+ Atk burned Kartana Giga Impact vs. 0 HP / 252 Def Arceus-Fighting: 80-95 (20.9 - 24.9%) -- guaranteed 5HKO

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
    example_3 = Damage.from_dict({
        "level": 100,
        "power": 110,
        "attack": stat_formula(92, 31, 0, 1, 100),
        "defense": stat_formula(85, 31, 0, 1, 100),
        "other_factors": damage_factors_test_values
    })
    # expected (127, 150) and (127, 129, 130, 132, 133, 135, 136, 138, 139, 141, 142, 144, 145, 147, 148, 150)
    print(example_3.damage_range)
    print(example_3.damage_array)


if __name__ == "__main__":
    main()
