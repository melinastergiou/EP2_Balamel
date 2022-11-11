from funcoes import * 
from base_dados import quest
from cores import *

# validando base de dados e ajustando
dic2 = valida_questoes(quest)
for elementos in dic2:
    if elementos=={}:
        dic = transforma_base(quest)

p = 'S'
while p=='S':
    
    ajudas = 2 
    pular = 3
    pontos = 0 # para dar certo o valor dos prêmios 
    premios = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    niveis= ['facil', 'medio', 'dificil']
    respostas = ['A', 'B', 'C', 'D']
    pergunta = 1 # número das questões
    sorteadas = [] # lista das perguntas já sorteadas
    
    print('\nBem vindo(a) ao...\n ' +GREEN+ ' $$ JOGO DA FORTUNA $$ '+RESET+ '\nAqui, você pode enrriquecer...\n')
    
    nome = input('Qual seu nome? ')
    print('\n')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
    print('As opções de resposta são' +BLUE+ ' "A", "B", "C", "D","ajuda", "pula" e "parar"'+RESET+'!')
    print('\n')
    enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
    nivel = niveis[0]
    print('\n')
    print(BOLD+ 'O jogo já vai começar! Lá vem a primeira questão!'+ RESET)
    print(f'Vamos começar com o nível {nivel}\n')
    enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
    premio=premios[pontos]
  
    sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)
    
    print(sorteio)
    questao= sorteio['titulo']
    opcoes = questao_para_texto(sorteio, pergunta)
    print(pergunta)
    correta = sorteio['correta']
    print(opcoes)
  
    resposta = input('\nQual a sua resposta? ')

    p2='N'

    while p2=='N':

        if  resposta==correta and pergunta<3:
                
            pontos+=1
            nivel = niveis[0]
            pergunta+=1
            premio=premios[pontos]
            print('\nVocê acertou! Seu prêmio atual é de '+ GREEN+ f'{premio}!'+RESET)

            enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
            
            sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)
            questao= sorteio['titulo']
            opcoes = questao_para_texto(sorteio, pergunta)

            correta = sorteio['correta']
            print(opcoes)
       

            resposta = input('\nQual a sua resposta? ') 
        
        elif resposta==correta and pergunta>=3 and pergunta<6:
            
            nivel = niveis[1]

            if pergunta>=3:        
                print(BOLD+f'WOW, você passou para o nível {nivel}!'+RESET)

            pontos+=1
            pergunta+=1
            premio=premios[pontos]
            print('\nVocê acertou! Seu prêmio atual é de '+ GREEN+ f'{premio}!'+RESET)

            enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
            
            sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)

            questao= sorteio['titulo']
            opcoes = questao_para_texto(sorteio, pergunta)

            correta = sorteio['correta']
            print(opcoes)
            

            resposta = input('\nQual a sua resposta? ') 

        elif resposta==correta and pergunta>=6 and pergunta<9: 
            nivel = niveis[2]

            if pergunta==6:
                print(BOLD+ f'\nWOW, você passou para o nível {nivel}!'+ RESET)

            pontos+=1

            pergunta+=1
            premio=premios[pontos]
            print('\nVocê acertou! Seu prêmio atual é de '+ GREEN+ f'{premio}!'+RESET)

            enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
            
            sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


            questao= sorteio['titulo']
            opcoes = questao_para_texto(sorteio, pergunta)

            correta = sorteio['correta']
            print(opcoes)
            

<<<<<<< HEAD
# indentificar nível anftes 
chama  = sorteia_questao(dic,nivel)
=======
            resposta = input('\nQual a sua resposta? ') 

        elif premio==1000000:
            print(BOLD+'\nPARABÉNS!'+RESET+ ' Você zerou o jogo e virou um '+GREEN+'MILIONÁRIO'+RESET)

        elif resposta =='ajuda':

            ajudas-=1
            
            
            if ajudas<0: 
                print(MAGENTA+'Ops! Você não tem mais direito a ajuda...\n'+RESET)
                enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)

                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                

                resposta = input('\nQual a sua resposta? ') 

            else:  
                print(f'\nOk, lá vem a ajuda! Você tem direito a mais {ajudas} ajudas')  
                dica= gera_ajuda(sorteio)
                print(dica)
                print(opcoes)
                resposta = input('\nQual a sua resposta? ') 
            

        elif resposta =='pula':

            pular-=1
            
            if pular> 0:    
                print(f'\nOk pulando...Você ainda tem {pular} pulos!')

                premio=premios[pontos]
                enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                

                resposta = input('\nQual a sua resposta? ')
            elif pular==0:
                print(f'\nOk pulando... ATENÇÃO: Você não tem mais pulos a partir de agora!')

                premio=premios[pontos]
                enter = input('Aperte' + YELLOW+ ' ENTER ' +RESET +'para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                

                resposta = input('\nQual a sua resposta? ')

            else:
                print(MAGENTA+'Ops.. Não deu!\nVocê não tem mais direito a pulos'+RESET)
                print(opcoes)
                resposta = input('\nQual a sua resposta? ')

        elif resposta!=correta and resposta in respostas:
            resposta = 'incorreta'
            print(RED+'Opa... você errou :(\nInfelizmente vai sair sem nada...'+RESET)
            break

        elif resposta=='parar':
            
            p2= input('Certeza que você deseja parar [S/N]?\nCaso sua resposta seja "S", você sairá com'+CYAN+' R$ {premio}'+RESET)
        
            if p2 =='N':
                resposta= input('\nQual a sua resposta? ')
            else:
                break
        
        else:
            print(CYAN+'Opção inválida!'+RESET)
            print('As opções de resposta são' +BLUE+ ' "A", "B", "C", "D","ajuda", "pula" e "parar"'+RESET+'!')
            resposta = input('\nQual a sua resposta? ')

    if resposta=='incorreta':
        p = input('\nDeseja reniciar o jogo [S/N]? ')
        if p=='N':
            print(f'\nOk você parou!')
    elif p2=='S':
        print(f'\nOk você parou!')
        break
    elif p=='N' or p2=='S':
            print(f'\nOk você parou! Seu prêmio é de {premio} reais.')
    
>>>>>>> cd7d248db647e17e06eedbf282c2d40475e8a185
