from math import pi

def get_tire_diameter(dist_before_turn, dist_after_turn):
    
    # TODO - there's a bug in this function! Find and fix it!
    
    circumference = dist_after_turn - dist_before_turn
    diameter = circumference * pi
    return diameter