def conta_caracteres(filename):
    with open(filename, 'r') as f:
        txt = f.read()
        lines = txt.splitlines()
        words = txt.split()    
    print('Quantidade de linhas: ', len(lines))
    print(words)
    print('Quantidade de palavras: ', len(words))
   
   
conta_caracteres(filename='D:/Qt34/UEM-FENG/UEM-FENG-5TH YEAR/Coding/basic-python/file_handling/obama_speech.txt')
conta_caracteres(filename='D:/Qt34/UEM-FENG/UEM-FENG-5TH YEAR/Coding/basic-python/file_handling/michelle_obama_speech.txt')

