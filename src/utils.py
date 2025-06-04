from packages import *

def my_round_down(value):
    frac = value - floor(value)
    if frac > 0.5:
        return ceil(value)
    return floor(value)

def my_round_up(value):
    frac = value - floor(value)
    if frac < 0.5:
        return floor(value)
    return ceil(value)