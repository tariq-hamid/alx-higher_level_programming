#!/usr/bin/python3
""" Module containing a function that prints a string """


def text_indentation(text):
    """Function that prints a text with 2
    new lines after each of these characters: ., ? and :

    Args:
        text: string to be printed

    Returns:
        nth
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    text = text.strip()
    pre = text[0]
    endings = ['.', '?', ':']

    for c in text:
        if c == ' ' and pre in endings:
            continue
        pre = c
        print(c, end='')
        if c in endings:
            print("\n")
