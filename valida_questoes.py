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

def valida_questoes(lista):
    saida = []
    i = 0
    for questao in lista:
        x = valida_questao(questao)
        saida.append(x)
    return saida