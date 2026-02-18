import re

regex_pattern = r'[^A-Za-z]|[-+]'
reg = r'^[A-Za-z][_]'
#regex_patter = r'[0-9].'

def is_valid_variable(variavel):
    if re.search(regex_pattern, variavel):
        print('False')
    else: 
        print('True')

is_valid_variable('firstname')