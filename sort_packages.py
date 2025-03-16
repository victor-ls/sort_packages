MAX_WEIGHT = 20
MAX_DIMENSION = 150
MAX_VOLUME = 1_000_000

def sort(width, height, length, mass):
    if not all(isinstance(x, (int, float)) for x in [width, height, length, mass]):
        raise ValueError("All inputs must be numeric.")
    
    if any(x < 0 for x in [width, height, length, mass]):
        raise ValueError("Dimensions and weight must be non-negative.")
    
    bulky = (width * height * length >= MAX_VOLUME or max(width, height, length) > MAX_DIMENSION)
    heavy = (mass >= MAX_WEIGHT)

    if bulky and heavy:
        return 'rejected'
    elif bulky or heavy:
        return 'special'
    return 'standard'
