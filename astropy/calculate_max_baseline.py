from geopy.distance import geodesic
from itertools import combinations

def calculate_max_baseline(coord_list):
    """
    Calculate the maximum geodesic distance (baseline) from a list of station coordinates.

    Parameters:
    - coord_list: list of (latitude, longitude) tuples

    Returns:
    - max_distance: maximum distance in meters
    - station_indices: indices of the two stations forming that baseline
    """
    max_distance = 0
    station_pair = (None, None)
    
    for (i1, coord1), (i2, coord2) in combinations(enumerate(coord_list), 2):
        distance = geodesic(coord1, coord2).meters
        if distance > max_distance:
            max_distance = distance
            station_pair = (i1, i2)
    
    return max_distance, station_pair

