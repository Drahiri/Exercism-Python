"""Functions used in preparing Guido's gorgeous lasagna.

Leard about Guido, the creator of the Pythona language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'

    Function that takes actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers to prepare.
    :return: int - time needed for preparation (in minutes) derived from 'PREPARATION_TIME'

    Function that takes number of layers in lasagna as an argument and returns
    how many minutes is needed to prepare them all based on 'PREPARATION_TIME'.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate elapsed time.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_time: int - time the lasagna spent baking in oven (in minutes).
    :return: int - total time elapsed (in minutes) preparing and cooking.

    Function that takes number of lasagna layers and time the lasagna spent
    already baking and returns how many minutes elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
