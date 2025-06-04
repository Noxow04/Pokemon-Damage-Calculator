# Pokemon Damage Calculator (WIP)

This project is a Pokemon damage calculator for a single attack.

<<<<<<< HEAD
Based on https://calc.pokemonshowdown.com for the idea. Developped, for now, for Generation 9 Singles only.

## Roadblocks
=======
Based on [Pokémon Showdown Damage Calculator](https://calc.pokemonshowdown.com) ([github](https://github.com/smogon/damage-calc)) for the idea. Developped, for now, for Generation 9 Singles only.

## Roadblocks

>>>>>>> release-0.1
- Full coverage testing
- Up to date documentation
- 'Pokemon' class with stats, typing, nature, etc
- 'Attack' class with power, typing, extra effects
- 'Item' class
- Database usage for type effectiveness
- Database usage to get a pokemon data directly from its name
- Visual interface
<<<<<<< HEAD
### Extras
- Speed optimiser
- Bulk optimiser
- Multiple languages support
=======

### Extras

- Speed optimiser
- Bulk optimiser
- Multiple languages support

## How to use

Use `src/formulas.py` as the entry point.  
Inside that file, modify the `main()` function.

To easily create **DamageFactors** and **ExtraFactors** instances, use of the `from_dict()` method is recommended.

### Basic funtions
Examples for how to use these functions can be found in `src/formulas.py` main function.

#### damage_formula()
Compute and return the expected damage from a certain attack explicitly given all parameters, namely : the level of the attacker, the base power of the attack, the relevant attack (attack or special attack) stat, the relevant defense (defense or special defense) stat and extra damage factors (cf damage_factors.py and extra_factors.py), including the 'random' factor.

#### attack_range()
Compute and return the minimum and maximum values of `damage_formula()`, using the minimum and maximum 'random' values (being 0.85 and 1 respectively).
If given a DamageFactor instance with a set random value, that value will be overwritten.

#### stat_formula()
Compute and return the value of any statistic (except HP) given its base value, the pokemon's level, the EVs and IVs, and the effect of the pokemon nature on that statistic (neutral, positive or negative) 

#### hp_formula()
Compute and return 

## How to run

### Basic run

To run the entry point, execute the formulas module in the src directory

```cmd
cd src
python -m formulas
```
>>>>>>> release-0.1
