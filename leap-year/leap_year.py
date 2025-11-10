def leap_year(year: int) -> bool:
    """Determines if year is a leap year.

    :param year: int - year to check if its leap year.
    :return: bool - is year a leap year?
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
