with open('C:/Users/Evineldy Nharreluga/Desktop/files/text.txt', 'w') as f:
    txt = f.write('Novo ficheiro \nEstudando de novo file handling')

with open('C:/Users/Evineldy Nharreluga/Desktop/files/text.txt', 'r') as f:
    txt = f.read().splitlines()
    print(txt)
    
    #print(nr_linhas)

with open('C:/Users/Evineldy Nharreluga/Desktop/files/text.txt', 'a') as f:
    txt = f.write('\nSubscrevendo o txt')



