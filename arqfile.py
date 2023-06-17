def arqexiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararq(nome):
    try:
        a=open(nome,'wt+')
    except:
        print('houve um erro na criação do arquivo')  
