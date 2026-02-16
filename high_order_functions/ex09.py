
#elementos = [['Neldy', 7]]
strings = []
def get_string_lists(elementos = []):
    for elemento in elementos:
        if type(elemento) == str:
            strings.append(elemento)
    return strings

get_string_lists(['Neldy', 7])

