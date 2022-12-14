import random
from cores import *

# TRANSFORMA BASE: 1ª FUNÇÃO
def transforma_base (lista):
    novodic={}

    for dics in lista:
        
        n = dics['nivel']

        if n not in novodic:
                
            novodic[n] =[]
                
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
    i = 0
    novalista=[]
    while i in range(len(lista)):
        questao = lista[i]
        ele = valida_questao(questao)
        novalista.append(ele)

        i = i +1

    return novalista    
# SORTEIA UMA QUESTÃO

def sorteia_questao(dic,nivel):
    questao = random.choice(dic[nivel])
    return questao

# SORTEIA UMA QUESTÃO INÉDITA
def sorteia_questao_inedita(dic,nivel,sorteadas):
    x = sorteia_questao(dic,nivel)
    while x in sorteadas:
        x = sorteia_questao(dic,nivel)
    sorteadas.append(x)
    return x

# STRING PARA TEXTO

def questao_para_texto(questao,n):
    pergunta = questao['titulo']
    A = questao['opcoes']['A']
    B = questao['opcoes']['B']
    C = questao['opcoes']['C']
    D = questao['opcoes']['D']

    saida = '----------------------------------------' +'\n'+BLUE+'QUESTAO' + ' ' + str(n)+RESET+ '\n' + '\n'+ pergunta+ '\n'+'\n'+'RESPOSTAS:' + '\n'+ 'A:' +' '+ A + '\n'+'B:' + ' '+ B + '\n' + 'C:'+' ' + C + '\n' + 'D:'+' ' + D
    return saida

# GERA AJUDA EM UMA QUESTÃO

def gera_ajuda (dic):

    corr= dic['correta'] 
    lista = []

    for c, v, in (dic['opcoes']).items():
        
        if c!=corr and c not in lista:

            lista.append(c)
        
        
    num= random.randint(1,2)
    if num ==1:
        dica= random.choice(lista)
            
    else:
        dica = []
        i = 0
        while len(dica)!= 2:
            item = random.choice(lista)
           
            if item not in dica:
                dica.append(item)
            i+=1
        
    if len(dica)==2:
        p1=dica[0] 
        p2=dica[1]
            
        v1 = dic['opcoes'][p1]
        v2 = dic['opcoes'][p2]
            
        r =( v1 + ' | ' + v2)
  
        return(f'DICA:\nOpções certamente erradas: {r}')
    else:
        v = dic['opcoes'][dica]
            
        return(f'DICA:\nOpções certamente erradas: {v}')
