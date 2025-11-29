COMMANDS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list[str]:
    """Translate binary into commands.

    :param binary_str: str - string of binary.
    :return: list[str] - list of commands to perform.
    """
    cmds = []
    for i in range(len(binary_str) - 1):
        if binary_str[-1 - i] == "1":
            cmds.append(COMMANDS[i])

    if binary_str[0] == "1":
        cmds.reverse()

    return cmds
