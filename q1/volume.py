def calc_volume(a):
    try:
        length = float(a)
    except ValueError:
        return "Enter a number."

    if(length <= 0):
        return "Enter a positive number greather than zero."
    else:
        return length * length * length