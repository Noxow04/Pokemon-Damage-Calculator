from packages import *

import extra_factors

class DamageFactors:
    def __init__(self):
        self._pb: Union[float, int] = 1
        self._weather: Union[float, int] = 1
        self._glaiverush: int = 1
        self._critical: Union[float, int] = 1
        self.random: Union[float, int] = None
        self._stab: Union[float, int] = 1
        self._type_effectiveness: Union[float, int] = 1
        self._burn: Union[float, int] = 1
        self._other: extra_factors.ExtraFactors = None
        self._zmove: Union[float, int] = 1
    
    def __repr__(self):
        return f"DamageFactors(pb={self.pb}, weather={self.weather}, glaiverush={self.glaiverush}, critical={self.critical}, random={self.random}, stab={self.stab}, type_effectiveness={self.type_effectiveness}, burn={self.burn}, other={self.other}, zmove={self.zmove})"
    
    @property
    def variables(self):
        """Returns a list of all factors"""
        return [self.pb, self.weather, self.glaiverush, self.critical, self.random, self.stab, self.type_effectiveness, self.burn, self.other, self.zmove]

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
    def weather(self, flag: int):
        """
        :param flag: -1 for negative weather | 0 for neutral/no weather | 1 for positive weather
        """
        match flag:
            case -1:
                self._weather = .5
            case 0:
                self._weather = 1
            case 1:
                self._weather = 1.5
            case _:
                raise ValueError(f"Weather flag must be -1, 0 or 1 | got {flag}")

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
    def critical(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._critical = 1.5
        else:
            self._critical = 1
        
    @property
    def stab(self):
        """STAB is the same-type attack bonus. This is equal to 1.5 if the move's type matches any of the user's types, 2 if the user of the move additionally has Adaptability, and 1 otherwise or if the attacker and/or used move is typeless. If the used move is a combination Pledge move, STAB is always 1.5 (or 2 if the user's Ability is Adaptability). When Terastallized, STAB is (if not 1): 1.5 if the move's type matches either the Pokemon's original type(s) or a different Tera Type from its original types, and the attacker's Ability is not Adaptability. 2 if the move's type matches the same Tera Type as one of the Pokemon's original types and the attacker's Ability is not Adaptability, or the situation above, if the attacker's Ability is Adaptability. However, if STAB only applies from the attacker's original type(s), not its Tera Type, STAB will always be 1.5, even if the attacker's Ability is Adaptability. 2.25 if the move's type matches the same Tera Type as one of the Pokemon's original types and the attacker's Ability is Adaptability."""
        return self._stab
    @stab.setter
    def stab(self, flag: int):
        """
        :param flag: 0 for no STAB | 1 for normal STAB | 2 for Adaptability STAB OR Tera Type | 3 for Adaptability STAB with Tera Type
        """
        match flag:
            case 0:
                self._stab = 1
            case 1:
                self._stab = 1.5
            case 2:
                self._stab = 2
            case 3:
                self._stab = 2.25
            case _:
                raise ValueError(f"STAB flag must be 0, 1, 2 or 3 | got {flag}")
        
    @property
    def type_effectiveness(self):
        """Type is the type effectiveness. This can be 0.125, 0.25, 0.5 (not very effective); 1 (normally effective); 2, 4, or 8 (super effective), depending on both the move's and target's types. The 0.125 and 8 can potentially be obtained on a Pokémon under the effect of Forest's Curse or Trick-or-Treat. If the used move is Struggle or typeless Revelation Dance, or the target is typeless, Type is always 1. Decimals are rounded down to the nearest integer. Certain effects can modify this, namely: If the target is an ungrounded Flying-type that is not being grounded by any other effect and is holding an Iron Ball or under the effect of Thousand Arrows, Type is equal to 1. If the target is a grounded Flying-type (unless grounded by an Iron Ball or Thousand Arrows, as above), treat Ground's matchup against Flying as 1. If the target is holding a Ring Target and the used move is of a type it would otherwise be immune to, treat that particular type matchup as 1. If the attacker's Ability is Scrappy, treat Normal and Fighting's type matchups against Ghost as 1. If the target is under the effect of Foresight, Odor Sleuth or Miracle Eye, and the target is of a type that would otherwise grant immunity to the used move, treat that particular type matchup as 1. If the used move is Freeze-Dry, treat the move's type's matchup against Water as 2. If the used move is Flying Press, consider both the move's type effectiveness and the Flying type's against the target, and multiply them together. If strong winds are in effect and the used move would be super effective against Flying, treat the type matchup against Flying as 1 instead. If the target is under the effect of Tar Shot and the used move is Fire-type, multiply Type by 2."""
        return self._type_effectiveness
    @type_effectiveness.setter
    def type_effectiveness(self, flag: int):
        """
        :param flag: -3 for 8 times resisted | -2 for 4 times resisted | -1 for 2 times resisted | 0 for neutral effectiveness | 1 for 2 times weak | 2 for 4 times weak | 3 for 8 times weak
        """
        match flag:
            case -3:
                self._type_effectiveness = .125
            case -2:
                self._type_effectiveness = .25
            case -1:
                self._type_effectiveness = .5
            case 0:
                self._type_effectiveness = 1
            case 1:
                self._type_effectiveness = 2
            case 2:
                self._type_effectiveness = 4
            case 3:
                self._type_effectiveness = 8
            case _:
                raise ValueError(f"Type flag must be an int between -3 and 3 | got {flag}")

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
    def other(self):
        if self._other is None:
            return 1
        return self._other.total()
    @other.setter
    def other(self, factors: extra_factors.ExtraFactors):
        assert(isinstance(factors, extra_factors.ExtraFactors))
        self._other = factors

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

    @staticmethod
    def from_dict(dictionary: dict):
        """Allow for a quick build of an instance via a dictionary (for testing purposes mainly)

        :param dictionary: dictionary with keys as attributes of the class
        """
        new_instance = DamageFactors()
        for key, value in dictionary.items():
            setattr(new_instance, key, value)
        return new_instance
