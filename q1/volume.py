def calc_volume(a):
    volume = 0
        
    try:
        length = float(a)
    except ValueError:
        raise ValueError("Enter a number")

    if(length <= 0):
        return "Enter a number greather than zero."
    else:
        volume = length * length * length
    
    return round(volume, 2)