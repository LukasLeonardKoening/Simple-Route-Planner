"""
planer.py - Calculates shortest route with A* algorithm
"""

# Import
from helpers import Map, load_map_10, load_map_40, show_map
import math
#%load_ext autoreload
#%autoreload 2

# Show map
map_40 = load_map_40()
show_map(map_40)