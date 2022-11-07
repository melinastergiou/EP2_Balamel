
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

# VALIDA UMA QUESTÃO

def valida_questao(dic):
    dic2 = {}
    niveis = ['facil','medio','dificil']
    respostas = ['A','B','C','D']
    if 'titulo' not in dic.keys():
        dic2['titulo'] = 'nao_encontrado'
    else:
        dic['titulo'] = dic['titulo'].strip()
        if dic['titulo'] == '':
            dic2['titulo'] = 'vazio'
    if 'nivel' not in dic.keys():
        dic2['nivel'] = 'nao_encontrado'
    else:
        if dic['nivel'] not in niveis:
            dic2['nivel'] = 'valor_errado'
    if 'opcoes' not in dic.keys():
        dic2['opcoes'] = 'nao_encontrado'
    else:
        if len(dic['opcoes'].values()) != 4:
            dic2['opcoes'] = 'tamanho_invalido'
        else:
            
            for letra in respostas:
                if letra not in dic['opcoes']:
                    dic2['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                else:
                    dic['opcoes'][letra] = dic['opcoes'][letra].strip()

                    if dic['opcoes'][letra] == '':
                        if 'opcoes' not in dic2.keys():
                            dic2['opcoes'] = {}
                            dic2['opcoes'][letra] = 'vazia' 
                        else:
                            dic2['opcoes'][letra] = 'vazia'
    if 'correta' not in dic.keys():
        dic2['correta'] = 'nao_encontrado'
    else:
        if dic['correta'] not in respostas:
            dic2['correta'] = 'valor_errado'
    if len(dic) != 4:
        dic2['outro'] = 'numero_chaves_invalido'
    return dic2
    

# VALIDA LISTA DE QUESTÕES 

def valida_questoes(lista):
    saida = []
    i = 0
    for questao in lista:
        x = valida_questao(questao)
        saida.append(x)
    return saida

# SORTEIA UMA QUESTÃO

import random
def sorteia_questao(dic,nivel):
    questao = random.choice(dic[nivel])
    return questao

# SORTEIA UMA QUESTÃO INÉDITA

def sorteia_questao_inedida(dic,nivel,sorteadas):
    x = sorteia_questao(dic,nivel)
    while x not in sorteadas:
        sorteadas.append(x)
        x = sorteia_questao(dic,nivel)
    return x

# STRING PARA TEXTO

def questao_para_texto(questao,n):
    pergunta = questao['titulo']
    A = questao['opcoes']['A']
    B = questao['opcoes']['B']
    C = questao['opcoes']['C']
    D = questao['opcoes']['D']

    saida = '----------------------------------------' +'\n'+'QUESTAO' + ' ' + str(n)+ '\n' + '\n'+ pergunta+ '\n'+'\n'+'RESPOSTAS:' + '\n'+ 'A:' +' '+ A + '\n'+'B:' + ' '+ B + '\n' + 'C:'+' ' + C + '\n' + 'D:'+' ' + D
    return saida