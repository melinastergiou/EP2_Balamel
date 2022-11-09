from funcoes import * 
from base_dados import quest

dic2 = valida_questoes(quest)
for elementos in dic2:
    if elementos=={}:
        dic = transforma_base(quest)
        
p = 'S'
while p=='S':
    
    ajudas = 2 # colocamos 3 para ajustar no código, mas apenas 2 estão sendo utilizadas
    pular = 3
    pontos = 0 # para dar certo o valor dos prêmios 
    premios = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    niveis= ['facil', 'medio', 'dificil']
    respostas = ['A', 'B', 'C', 'D']
    pergunta = 1 # número das questões
    sorteadas = [] # lista das perguntas já sorteadas
    
    print('Bem vindo ao $$ JOGO DA FORTUNA $$ de dsoft!\nAqui, você pode enrriquecer...\n')
    nome = input('Qual seu nome? ')
    print('\n')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
    print('As opções de resposta são  "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    print('\n')
    enter = input('Aperte ENTER para continuar...')
    nivel = niveis[0]
    print('\n')
    print('O jogo já vai começar! Lá vem a primeira questão!')
    print(f'Vamos começar com o nível {nivel}\n')
    enter = input('Aperte ENTER para continuar...')
    premio=premios[pontos]
  
    sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)
    
    # FALTA USAR O VALIDA QUESTÃO MEEEEEL
    # valida= valida_questao(sorteio)

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

    p2='N'

    while p2=='N':

        if  resposta==correta and pergunta<3:
                
            pontos+=1
            nivel = niveis[0]
            pergunta+=1
            premio=premios[pontos]
            print(f'\nVocê acertou! Seu prêmio atual é de {premio}!')

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
            print(f'\nVocê acertou! Seu prêmio atual é de {premio}!')
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
                print(f'\nWOW, você passou para o nível {nivel}!')

            pontos+=1

            pergunta+=1
            premio=premios[pontos]
            print(f'\nVocê acertou! Seu prêmio atual é de {premio}!')
            enter = input('Aperte ENTER para continuar...')
            
            sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


            questao= sorteio['titulo']
            opcoes = questao_para_texto(sorteio, pergunta)

            correta = sorteio['correta']
            print(opcoes)
            print(correta)

            resposta = input('\nQual a sua resposta? ') 

        elif premio==1000000:
            print('\nPARABÉNS! Você zerou o jogo e virou um MILIONÁRIO')

        elif resposta =='ajuda':

            ajudas-=1
            
            
            if ajudas<0: 
                print('Ops! Você não tem mais direito a ajuda...\n')
                enter = input('Aperte ENTER para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)

                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                print(correta)

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
                enter = input('Aperte ENTER para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                print(correta)

                resposta = input('\nQual a sua resposta? ')
            elif pular==0:
                print(f'\nOk pulando... ATENÇÃO: Você não tem mais pulos a partir de agora!')

                premio=premios[pontos]
                enter = input('Aperte ENTER para continuar...')
                
                sorteio = sorteia_questao_inedita(dic,nivel,sorteadas)


                questao= sorteio['titulo']
                opcoes = questao_para_texto(sorteio, pergunta)

                correta = sorteio['correta']
                print(opcoes)
                print(correta)

                resposta = input('\nQual a sua resposta? ')

            else:
                print('Ops.. Não deu!\nVocê não tem mais direito a pulos')
                print(opcoes)
                resposta = input('\nQual a sua resposta? ')

        elif resposta!=correta and resposta in respostas:
            resposta = 'incorreta'
            print('Opa... você errou :(\nInfelizmente vai sair sem nada...')
            break

        elif resposta=='parar':
            
            p2= input(f'Certez que você deseja parar [S/N]? Caso sua resposta seja "S", você sairá com R$ {premio}')
        
            if p2 =='N':
                resposta= input('\nQual a sua resposta? ')
            else:
                break
        
        else:
            print('Opção inválida!')
            print('As opcções de resposta são  "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
            resposta = input('\nQual a sua resposta? ')

    if resposta=='incorreta':
        p = input('Deseja reniciar o jogo [S/N]? ')

    elif p=='S' or p2=='S':
            print(f'\nOk você parou! Seu prêmio é de {premio} reais.')

    # else:
    # # deveria retornar tudo do início (parte de onde parou na pergunta que parou !!!!!!!!!!!!)

    #         print(f'\nOk você parou! Seu prêmio é de {premio} reais.')
    #         p='N'

   