# Pokemon Damage Calculator (WIP)

This project is a Pokemon damage calculator for a single attack.

Based on [Pokémon Showdown Damage Calculator](https://calc.pokemonshowdown.com) ([github](https://github.com/smogon/damage-calc)) for the idea. Developped, for now, for Generation 9 Singles only.

## Roadblocks

- Full coverage testing
- Up to date documentation
- 'Pokemon' class with stats, typing, nature, etc
- 'Attack' class with power, typing, extra effects
- 'Item' class
- Database usage for type effectiveness
- Database usage to get a pokemon data directly from its name
- Visual interface

### Extras

- Speed optimiser
- Bulk optimiser
- Multiple languages support

## How to run

### Basic run

To run what I used as my entry point, execute the formulas module in the src directory

```cmd
cd src
python -m formulas [args]
```

#### [args]

- ```no-ic```  
If you wish not to (or can't) use the 'icecream' module

### Tests

```cmd
cd test
python -m unittest -v
```
