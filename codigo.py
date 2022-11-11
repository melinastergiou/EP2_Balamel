from funcoes import * 
from base_dados import quest

dic = transforma_base(quest)



nome = input('Qual seu nome? ')
print('\n')
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('\n')
print('As opcções de resposta são  "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
print('\n')
enter = input('Aperte ENTER para continuar...')
print('\n')
print('O jogo já vai começar! Lá vem a primeira questão!')
print('\n')
print('Vamos começar com o nível FÁCIL!')
enter = input('Aperte ENTER para continuar...')
print('\n')
print('\n')
print('------------------------------------------------')
print('\n')
print('QUESTÃO 1')

# indentificar nível anftes 
chama  = sorteia_questao(dic,nivel)