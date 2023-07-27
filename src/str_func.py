def str_upper(text):
    try:
        result = text.upper()
    except AttributeError:
        return "Attribute must be 'str'."
    else:
        return result
