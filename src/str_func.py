def str_upper(text):
    """
    Принимает строку и возвращает 
    ее со всеми заглавными буквами.
    """
    try:
        result = text.upper()
    except AttributeError:
        return "Attribute must be 'str'."
    else:
        return result
