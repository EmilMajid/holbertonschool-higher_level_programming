#!/usr/bin/python3
'''
This is the "5-text_indentation" module.
The example module supplies one function, def text_indentation().
'''


def text_indentation(text):
    '''
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    for line in text.strip().splitlines():
        print(line.strip(), end="")
