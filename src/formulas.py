from math import floor
from operator import itemgetter
from typing import Annotated, Union

from icecream import ic


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


class DamageFactors:
    def __init__(self):
        self._pb: Union[float, int] = 1
        self._weather: Union[float, int] = 1
        self._glaiverush: int = 1
        self._critical: Union[float, int] = 1
        self.random: Union[float, int] = None
        self._stab: Union[float, int] = 1
        self._type: Union[float, int] = 1
        self._burn: Union[float, int] = 1
        self.other: ExtraFactors = None
        self._zmove: Union[float, int] = 1

        self.variables = (self.pb, self.weather, self.glaiverush, self.critical, self.random, self.stab, self.type, self.burn, self.other, self.zmove)
    @property
    def pb(self):
        """PB is 0.25 if the move is the second strike of Parental Bond, and 1 otherwise."""
        return self._pb
    @pb.setter
    def pb(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._pb = 0.25
        else:
            self._pb = 1

    @property
    def weather(self):
        """Weather is 1.5 if a Water-type move is being used during rain or a Fire-type move or Hydro Steam during harsh sunlight, and 0.5 if a Water-type move (besides Hydro Steam) is used during harsh sunlight or a Fire-type move during rain, and 1 otherwise or if any Pokémon on the field have the Ability Cloud Nine or Air Lock."""
        return self._weather
    @weather.setter
    def weather(self, value: Union[float, int]):
        if value in (1, 1.5, 0.5):
            self._weather = value
        else:
            raise ValueError(f"Weather must be 1, 1.5 or 0.5 | got {value}")

    @property
    def glaiverush(self):
        """GlaiveRush is 2 if the target used the move Glaive Rush in the previous turn, or 1 otherwise."""
        return self._glaiverush
    @glaiverush.setter
    def glaiverush(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._glaiverush = 2
        else:
            self._glaiverush = 1

    @property
    def critical(self):
        """Critical is 1.5 for a critical hit, and 1 otherwise. Decimals are rounded down to the nearest integer. It is always 1 if the target's Ability is Battle Armor or Shell Armor or if the target is under the effect of Lucky Chant. Conversely, unless critical hits are prevented entirely by one of the above effects, Critical will always be 1.5 if the used move is Storm Throw, Frost Breath, Zippy Zap, Surging Strikes, Wicked Blow, or Flower Trick, the target is poisoned and the attacker's Ability is Merciless, or if the user is under the effect of Laser Focus."""
        return self._critical
    @critical.setter
    def critical(self, value: Union[float, int]):
        if value in (1, 1.5):
            self._critical = value
        else:
            raise ValueError(f"Critical must be 1 or 1.5 | got {value}")
        
    @property
    def stab(self):
        """STAB is the same-type attack bonus. This is equal to 1.5 if the move's type matches any of the user's types, 2 if the user of the move additionally has Adaptability, and 1 otherwise or if the attacker and/or used move is typeless. If the used move is a combination Pledge move, STAB is always 1.5 (or 2 if the user's Ability is Adaptability). When Terastallized, STAB is (if not 1): 1.5 if the move's type matches either the Pokemon's original type(s) or a different Tera Type from its original types, and the attacker's Ability is not Adaptability. 2 if the move's type matches the same Tera Type as one of the Pokemon's original types and the attacker's Ability is not Adaptability, or the situation above, if the attacker's Ability is Adaptability. However, if STAB only applies from the attacker's original type(s), not its Tera Type, STAB will always be 1.5, even if the attacker's Ability is Adaptability. 2.25 if the move's type matches the same Tera Type as one of the Pokemon's original types and the attacker's Ability is Adaptability."""
        return self._stab
    @stab.setter
    def stab(self, value: Union[float, int]):
        if value in (1, 1.5, 2, 2.25):
            self._stab = value
        else:
            raise ValueError(f"STAB must be 1, 1.5, 2 or 2.25 | got {value}")
        
    @property
    def type(self):
        """Type is the type effectiveness. This can be 0.125, 0.25, 0.5 (not very effective); 1 (normally effective); 2, 4, or 8 (super effective), depending on both the move's and target's types. The 0.125 and 8 can potentially be obtained on a Pokémon under the effect of Forest's Curse or Trick-or-Treat. If the used move is Struggle or typeless Revelation Dance, or the target is typeless, Type is always 1. Decimals are rounded down to the nearest integer. Certain effects can modify this, namely: If the target is an ungrounded Flying-type that is not being grounded by any other effect and is holding an Iron Ball or under the effect of Thousand Arrows, Type is equal to 1. If the target is a grounded Flying-type (unless grounded by an Iron Ball or Thousand Arrows, as above), treat Ground's matchup against Flying as 1. If the target is holding a Ring Target and the used move is of a type it would otherwise be immune to, treat that particular type matchup as 1. If the attacker's Ability is Scrappy, treat Normal and Fighting's type matchups against Ghost as 1. If the target is under the effect of Foresight, Odor Sleuth or Miracle Eye, and the target is of a type that would otherwise grant immunity to the used move, treat that particular type matchup as 1. If the used move is Freeze-Dry, treat the move's type's matchup against Water as 2. If the used move is Flying Press, consider both the move's type effectiveness and the Flying type's against the target, and multiply them together. If strong winds are in effect and the used move would be super effective against Flying, treat the type matchup against Flying as 1 instead. If the target is under the effect of Tar Shot and the used move is Fire-type, multiply Type by 2."""
        return self._type
    @type.setter
    def type(self, value: Union[float, int]):
        if value in (.125, .25, .5, 1, 2, 4, 8):
            self._type = value
        else:
            raise ValueError(f"Type must be 0.125, 0.25, 0.5, 1, 2, 4 or 8 | got {value}")

    @property
    def burn(self):
        """Burn is 0.5 if the attacker is burned, its Ability is not Guts, and the used move is a physical move (other than Facade), and 1 otherwise."""
        return self._burn
    @burn.setter
    def burn(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._burn = .5
        else:
            self._burn = 1

    @property
    def zmove(self):
        """ZMove is 0.25 if the move is a Z-Move or Max Move and the target would be protected from that move (e.g. by Protect), and 1 otherwise. (If this multiplier is applied, a message is displayed that the target "couldn't fully protect" itself.)"""
        return self._zmove
    @zmove.setter
    def zmove(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._zmove = 0.25
        else:
            self._zmove = 1


class ExtraFactors:
    def __init__(self):
        """other is 1 in most cases, and a different multiplier when specific interactions of moves, Abilities, or items take effect, in this order (and if multiple moves, Abilities, or items take effect, they do so in the order of the out-of-battle Speed stats of the Pokémon with them): If multiple effects influence the other value, their values stack multiplicatively, in the order listed above. This is done by starting at 4096, multiplying it by each number above in the order listed above, and rounding to the nearest integer whenever the result is not an integer (rounding up at 0.5). When the final value is obtained, it is divided by 4096, and this becomes other. For example, if both Multiscale and a Chilan Berry take effect, other is 4096×0.5×0.54096 = 0.25."""
        self._dynamax = 1
        self._minimize = 1
        self._dig_dive = 1
        self._screens = 1
        self._paradox_duo_attack = 1
        self._multiscale_and_others = 1
        self._filter_and_others = 1
        self._neuroforce = 1
        self._sniper = 1
        self._tinted_lens = 1
        self._fluffy = 1
        self._type_berry = 1
        self._expert_belt = 1
        self._life_orb = 1
        self._metronome = 1
        
        self.variables = self.dynamax, self.minimize, self.dig_dive, self.screens, self.paradox_duo_attack, self.multiscale_and_others, self.filter_and_others, self.neuroforce, self.sniper, self.tinted_lens, self.fluffy, self.type_berry, self.expert_belt, self.life_orb, self.metronome

    @property
    def dynamax(self):
        """2 if the target is Dynamaxed and the used move is Behemoth Blade, Behemoth Bash or Dynamax Cannon"""
        return self._dynamax
    @dynamax.setter
    def dynamax(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._dynamax = 2
        else:
            self._dynamax = 1

    @property
    def minimize(self):
        """2 if the target has used Minimize and the used move is Body Slam, Stomp, Dragon Rush, Heat Crash, Heavy Slam, Flying Press or Supercell Slam"""
        return self._minimize
    @minimize.setter
    def minimize(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._minimize = 2
        else:
            self._minimize = 1

    @property
    def dig_dive(self):
        """2 if the target is in the semi-invulnerable turn of Dig and the used move is Earthquake or Magnitude OR if the target is in the semi-invulnerable turn of Dive and the used move is Surf or Whirlpool"""
        return self._dig_dive
    @dig_dive.setter
    def dig_dive(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._dig_dive = 2
        else:
            self._dig_dive = 1

    @property
    def screens(self):
        """0.5 if in effect on the target's side, the used move is physical (Reflect), special (Light Screen), or either (Aurora Veil), the move is not a critical hit, and the user's Ability is not Infiltrator. Does not stack, even if e.g. Light Screen and Aurora Veil are active at the same time."""
        return self._screens
    @screens.setter
    def screens(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._screens = .5
        else:
            self._screens = 1
    
    @property
    def paradox_duo_attack(self):
        """5461/4096 if either Collision Course or Electro Drift is the used move and it is super effective"""
        return self._paradox_duo_attack
    @paradox_duo_attack.setter
    def paradox_duo_attack(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._paradox_duo_attack = 5461/4096
        else:
            self._paradox_duo_attack = 1

    @property
    def multiscale_and_others(self):
        """0.5 if the target has Multiscale and Shadow Shield and is at full health ORi f the target has Fluffy and the used move makes contact OR if the target has Punk Rock and the used move is sound-based OR if the target has Ice Scales and the used move is a special move"""
        return self._multiscale_and_others
    @multiscale_and_others.setter
    def multiscale_and_others(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._multiscale_and_others = .5
        else:
            self._multiscale_and_others = 1

    @property
    def filter_and_others(self):
        """0.75 if the target has Filter, Prism Armor or Solid Rock and the used move is super effective (Type > 1)"""
        return self._filter_and_others
    @filter_and_others.setter
    def filter_and_others(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._filter_and_others = .75
        else:
            self._filter_and_others = 1
    
    @property
    def neuroforce(self):
        """1.25 if the user has Neuroforce and the used move is super effective (Type > 1)"""
        return self._neuroforce
    @neuroforce.setter
    def neuroforce(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._neuroforce = 1.25
        else:
            self._neuroforce = 1

    @property
    def sniper(self):
        """1.5 if the attacker has Sniper and the move lands a critical hit"""
        return self._sniper
    @sniper.setter
    def sniper(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._sniper = 1.5
        else:
            self._sniper = 1

    @property
    def tinted_lens(self):
        """2 if the attacker has this Ability and the used move is not very effective (Type < 1)"""
        return self._tinted_lens
    @tinted_lens.setter
    def tinted_lens(self, flag):
        assert(isinstance(flag, bool))
        if flag:
            self._tinted_lens = 2
        else: 
            self._tinted_lens = 1

    @property
    def fluffy(self):
        pass



def damage_formula(level, power, attack, defense, other_factors: Annotated[list[Union[float, None, list]], 12]):
    result = ((((2 * level) / 5 + 2) * power * (attack / defense)) / 50 + 2)
    duplicate_factors = list(other_factors)
    extra_factors = duplicate_factors.pop(9)
    ic(extra_factors)
    for factor in duplicate_factors:
        result = floor(result * factor)
    if not extra_factors:
        return result
    else:
        extra_factors = sorted(extra_factors, key=itemgetter(1))
        for factor in itemgetter(0)(extra_factors):
            result = floor(result * factor)


def attack_range(factors: Annotated[list[Union[float, None, list]], 12], level, power, attack, defense):
    factors[5] = .85
    min_damage = damage_formula(level, power, attack, defense, factors)
    factors[5] = 1
    max_damage = damage_formula(level, power, attack, defense, factors)
    return min_damage, max_damage


if __name__ == "__main__":
    ic.configureOutput(includeContext=True)
    print('testing :')
    # abomasnow on abomasnow blizzard test
    print("expected (127-150) | got",
          attack_range([1, 1, 1, 1, 1, 1, 1.5, 1, 1, None, 1, 1], 100, 110, stat_formula(92, 31, 0, 1, 100),
                       stat_formula(85, 31, 0, 1, 100)))
