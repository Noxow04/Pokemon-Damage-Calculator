import utils

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
        
    def __repr__(self):
        return f"ExtraFactors(dynamax={self.dynamax}, minimize={self.minimize}, dig_dive={self.dig_dive}, screens={self.screens}, paradox_duo_attack={self.paradox_duo_attack}, multiscale_and_others={self.multiscale_and_others}, filter_and_others={self.filter_and_others}, neuroforce={self.neuroforce}, sniper={self.sniper}, tinted_lens={self.tinted_lens}, fluffy={self.fluffy}, type_berry={self.type_berry}, expert_belt={self.expert_belt}, life_orb={self.life_orb}, metronome={self.metronome})"

    @property
    def variables(self):
        """Returns a list of all factors"""
        return [self.dynamax, self.minimize, self.dig_dive, self.screens, self.paradox_duo_attack, self.multiscale_and_others, self.filter_and_others, self.neuroforce, self.sniper, self.tinted_lens, self.fluffy, self.type_berry, self.expert_belt, self.life_orb, self.metronome]

    @property
    def dynamax(self):
        """2 if the target is Dynamaxed and the used move is Behemoth Blade, Behemoth Bash or Dynamax Cannon"""
        return self._dynamax
    @dynamax.setter
    def dynamax(self, flag: bool):
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
    def minimize(self, flag: bool):
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
    def dig_dive(self, flag: bool):
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
    def screens(self, flag: bool):
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
    def paradox_duo_attack(self, flag: bool):
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
    def multiscale_and_others(self, flag: bool):
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
    def filter_and_others(self, flag: bool):
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
    def neuroforce(self, flag: bool):
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
    def sniper(self, flag: bool):
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
    def tinted_lens(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._tinted_lens = 2
        else: 
            self._tinted_lens = 1

    @property
    def fluffy(self):
        """2 if the target has Fluffy and the used move is Fire-type"""
        return self._fluffy
    @fluffy.setter
    def fluffy(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._fluffy = 2
        else:
            self._fluffy = 1
    
    @property
    def type_berry(self):
        """0.5 (0.25 if the holder has Rippen) if held by the target, the move is of the corresponding type, and is super effective (Type > 1); for the Chilan Berry, the used move must simply only be Normal-type"""
        return self._type_berry
    @type_berry.setter
    def type_berry(self, flag: int):
        """
        :param flag: 0 if nothing | 1 if holding a berry | 2 if holding a berry and rippen
        """
        match flag:
            case 0:
                self._type_berry = 1
            case 1:
                self._type_berry = .5
            case 2:
                self._type_berry = .25
            case _:
                raise ValueError(f"Type-Berry flag must be 0, 1 or 2 | got {flag}")
    
    @property
    def expert_belt(self):
        """4915/4096 if held by the attacker and the move is super effective (Type > 1)"""
        return self._expert_belt
    @expert_belt.setter
    def expert_belt(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._expert_belt = 4915/4096
        else:
            self._expert_belt = 1

    @property
    def life_orb(self):
        """5324/4096 if held by the attacker"""
        return self._life_orb
    @life_orb.setter
    def life_orb(self, flag: bool):
        assert(isinstance(flag, bool))
        if flag:
            self._life_orb = 5324/4096
        else:
            self._life_orb = 1

    @property
    def metronome(self):
        """1 + (819/4096 (~0.2) per successful consecutive use of the same move) if held by the attacker, but no more than 2"""
        return self._metronome
    @metronome.setter
    def metronome(self, uses: int):
        if uses < 0 or not isinstance(uses, int):
            raise ValueError(f"Metronome uses must be a positive integer | got {uses}")
        if uses == 0:
            self._metronome = 1
        else:
            self._metronome = min(2, 1 + (819 / 4096) * uses)

    def total(self):
        """Returns the total of all factors"""
        result = 4096
        for factor in self.variables:
            assert(factor)
            if factor != 1:
                result = utils.my_round_up(result * factor)
        return result / 4096
    
    @staticmethod
    def quick_setup(dictionary: dict):
        """Allow for a quick build of an instance via a dictionary (for testing purposes mainly)

        :param dictionary: dictionary with keys as attributes of the class
        """
        new_instance = ExtraFactors()
        for key, value in dictionary.items():
            setattr(new_instance, key, value)
        return new_instance