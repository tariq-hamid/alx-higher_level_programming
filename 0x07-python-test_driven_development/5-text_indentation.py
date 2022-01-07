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
    strings_ = []
    line = ""
    for c in text:
        line += c
        strings_.append(line.strip())
        if c in [".", "?", ":"]:
            line = ""
    for line_ in strings_:
        print("{}\n".format(line_))
    
