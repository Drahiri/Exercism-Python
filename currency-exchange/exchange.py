"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculates amount of exchanged money in foreign currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    Function that takes amount of money to be exchange and exchange rate as arguments,
    and returns the value of foreign currency you can receive.
    Exchange rate defines how much you must spent to receive 1 unit of foreign currency.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculates amount of money left after exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange.
    :return: float - amount left of your starting currency after exchanging.

    Function that takes amount to money to be exchange and how much money has been
    exchanged, and returns how much money remain.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculates the value of bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of bills.

    Function that takes denomination and number of bills, and returns value
    of bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    pass


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    pass


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    pass
