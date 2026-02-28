from collections import Counter

import re 

def top_10_palavras(caminho):
    with open(caminho, 'r', encoding='UTF-8') as f:
        texto = f.read().lower()

    palavras = re.findall(r'\b\w+\b', texto)

    contagem = Counter(palavras)
    return contagem.most_common(5)

resultado = top_10_palavras('D:/Qt34/UEM-FENG/UEM-FENG-5TH YEAR/Coding/basic-python/file_handling/obama_speech.txt')

for palavra, freq in resultado:
    print(palavra, '->', freq)



