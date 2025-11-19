def convert(number: int) -> str:
    """Converts number into sounds.

    :param number: int - number to convert.
    :return: str - sound.

    Rules for number to sound convert:
    * if divisible by 3 - sound 'Pling'.
    * if divisible by 5 - sound 'Plang'.
    * if divisible by 7 - sound 'Plong'.
    * if neither of above - number as string.
    """
    dividers = {3: "Pling", 5: "Plang", 7: "Plong"}
    ret_sound = ""

    for divider, sound in dividers.items():
        ret_sound += sound if number % divider == 0 else ""

    return ret_sound or str(number)
