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
    result = ''
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'

    for line in result.strip().split('\n'):
        print(line.strip())
