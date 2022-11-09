from funcoes import * 
from base_dados import quest

dic = transforma_base(quest)

ajudas = 2
pular = 3
pontos = -1 # para dar certo o valor dos prêmios 
premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
niveis= ['facil', 'medio', 'dificil']
nome = input('Qual seu nome? ')
respostas = ['A', 'B', 'C', 'D']

pergunta = 1 # número das questões
sorteadas = [] # lista das perguntas já sorteadas

print('\n')
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('\n')
print('As opcções de resposta são  "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
print('\n')
enter = input('Aperte ENTER para continuar...')
nivel = niveis[0]
print('\n')
print('O jogo já vai começar! Lá vem a primeira questão!')
print('\n')
print(f'Vamos começar com o nível {nivel}')
enter = input('Aperte ENTER para continuar...')

sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)
print(sorteio)
questao= sorteio['titulo']
opcoes = questao_para_texto(sorteio, pergunta)
print(pergunta)
correta = sorteio['correta']
print(questao)
print(opcoes)
print(correta)
print(pergunta)
resposta = input('\nQual a sua resposta? ')

while resposta!='parar':

    if  resposta==correta and pergunta<3:
            
        pontos+=1
        nivel = niveis[0]
        pergunta+=1
        premio=premios[pontos]
        print(f'Você acertou! Seu prêmio atual é de {premio}!')

        enter = input('Aperte ENTER para continuar...')
        
        sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


        questao= sorteio['titulo']
        opcoes = questao_para_texto(sorteio, pergunta)

        correta = sorteio['correta']
        print(opcoes)
        print(correta)

        resposta = input('\nQual a sua resposta? ') 
    
    elif resposta==correta and pergunta>=3 and pergunta<6:
        
        nivel = niveis[1]

        if pergunta>=3:        
            print(f'WOW, você passou para o nível {nivel}!')

        pontos+=1
        pergunta+=1
        premio=premios[pontos]
        print(f'Você acertou! Seu prêmio atual é de {premio}!')
        enter = input('Aperte ENTER para continuar...')
        
        sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)

        questao= sorteio['titulo']
        opcoes = questao_para_texto(sorteio, pergunta)

        correta = sorteio['correta']
        print(opcoes)
        print(correta)

        resposta = input('\nQual a sua resposta? ') 

    elif resposta==correta and pergunta>=6 and pergunta<9: 
        nivel = niveis[2]

        if pergunta==6:
            print(f'WOW, você passou para o nível {nivel}!')

        pontos+=1

        pergunta+=1
        premio=premios[pontos]
        print(f'Você acertou! Seu prêmio atual é de {premio}!')
        enter = input('Aperte ENTER para continuar...')
        
        sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


        questao= sorteio['titulo']
        opcoes = questao_para_texto(sorteio, pergunta)

        correta = sorteio['correta']
        print(opcoes)
        print(correta)

        resposta = input('\nQual a sua resposta? ') 

    elif pontos==7:
        print('PARABÉNS! Você zerou o jogo e virou um MILIONÁRIO')

    elif resposta =='ajuda':

        ajudas-=1
        print(f'Ok, lá vem a ajuda! Você tem direito a mais {ajudas} ajudas')
        
        if ajudas<=0: 
            print('Não deu! Você não tem mais direito a ajuda')
            enter 

        else:    
            dica= gera_ajuda(sorteio)
            print(dica)
            print(opcoes)
            resposta = input('\nQual a sua resposta? ') 
        

    elif resposta =='pular':

        pular-=1

        print(f'Ok pulando...Você ainda tem {pular} pulos!')

        premio=premios[pontos]
        enter = input('Aperte ENTER para continuar...')
        
        sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


        questao= sorteio['titulo']
        opcoes = questao_para_texto(sorteio, pergunta)

        correta = sorteio['correta']
        print(opcoes)
        print(correta)

        resposta = input('\nQual a sua resposta? ')
    
    elif resposta!=correta and resposta in respostas:
        resposta = 'incorreta'
        print('Opa... você errou :(')
        break


if resposta=='incorreta':
    p = input('Deseja reniciar o jogo [S/N]? ')
else:
    p = input('Certez que você deseja parar [S/N]? ')

if p=='S':
    print('Uma pena... qualquer coisa só me reniciar')
else:


    


    #     if resposta=='parar':

    

# elif pergunta >3 and pergunta<6:
#     nivel=niveis[1]
#     print(f'Hey! Você passou para no nível {nivel}')
#     enter = input('Aperte ENTER para continuar...')

#     sorteio = sorteia_questao_inedida(dic,nivel,sorteadas)
    
#     questao= sorteio['titulo']
#     opcoes = sorteio['opcoes']

# else:
#     nivel = niveis[2]
#     print(f'Hey! Você passou para no nível {nivel}')
#     enter = input('Aperte ENTER para continuar...')

    
#     sorteio = sorteia_questao_inedida(dic,nivel,sorteadas)
    
    
#     pergunta= sorteio['titulo']
#     opcoes = sorteio['opcoes']

# print('\n')
# print('\n')
# print('------------------------------------------------')
# print('\n')

