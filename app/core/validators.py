def validate_int(value: str):
    """
    Validate and convert input value into integer
    :param value: user input value
    :return: integer value otherwise None
    """
    try:
        return int(value)

    except ValueError:
        return None


def validate_float(value: str):
    """
    Validate and convert input value into float
    :param value: user input value
    :return: float value otherwise None
    """
    try:
        return float(value)

    except ValueError:
        return None

# def validate_string(value: str):
#     pass
