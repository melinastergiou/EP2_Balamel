
# TRANSFORMA BASE: 1ª FUNÇÃO
def transforma_base (lista):
    novodic={}

    for dics in lista:
        
        n = dics['nivel']

        if n not in novodic:
                
            novodic[n] =[]
            print(dics)
                
            novodic[n].append(dics)
        else:
            novodic[n].append(dics)            
    return novodic