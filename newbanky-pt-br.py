from datetime import datetime
from time import sleep

pergunta1=int()
estado = 'não logado'
token = ''
nome = ''
senha = ''

while True:
    if estado == 'não logado':
        print(f'''Estado: {estado.upper()} 
        
        [ 0 ] Registro
        [ 1 ] Login
        [ 2 ] Sair
        ''')
        pergunta = int(input('Escolha: '))
    if estado == 'não logado':
        if pergunta == 0:
                while True: # Pergunta os dados 
                
                    nome = str(input('Nome: '))
                    dia = int(input('Dia de nascimento: '))
                    mes = str(input('Mês de nascimento: '))
                    ano = int(input('Ano de nascimento: '))
                    idade = datetime.now().year - ano
                    senha = ''
                    conf = ''
                    saldo = float()

                    while len(senha) < 8: # Pergunta a senha
                        senha = str(input('Digite sua senha(Mínimo 8 caracteres): '))
                    while senha != conf: # Confirma a senha
                        conf = str(input('Digite sua senha denovo para confirmar: '))
                    token = nome + senha + 'tokenvalido123' # Cria um token improvisado
                    lista = [nome,idade,senha,saldo]
                

                    print(f'''
                    Nome: {nome}
                    Nasceu no dia {dia} de {mes} de {ano}
                    Senha: {senha}
                    ''') # Exibe os dados
                    c = input('Correto? [S/N]  ').upper().strip()[0] # Confirma os dados
                    if c in 'Ss':
                        print('CADASTRO COMPLETO')
                        arquivo = open('dados.txt','a')
                        arquivo.write(f'{lista}') # Guarda os dados em um arquivo txt
                        break
        elif pergunta == 1:
            print('--'*15)
            nome_log = ''
            senha_log = ''
            print(' - - Faça seu login - - ')
            while True:
                nome_log = input('Nome: ')
                senha_log = input('Senha: ')
                token1 = nome_log+senha_log+'tokenvalido123'
                if token1 == 'tokenvalido123':
                    print('Oh!Você não tem conta ')
                    print('Que tal... ',end='',flush='False')
                    sleep(2)
                    print('Voltar',flush='False')
                    sleep(2.5)
                    break
                elif token1 == token:
                    estado = 'logado'
                    break
                print('Digite a senha ou nome corretamente! ')
                print('\nSE NÃO TIVER UMA CONTA PRESSIONE ENTER! ')
                print('--'*15)
        elif pergunta == 2:
            break  
    if estado == 'logado':
        print(f''' Estado: {estado}
        [ 0 ] Minhas informações
        [ 1 ] Depositar
        [ 2 ] Transferir
        [ 3 ] Sair
        ''')
        pergunta1 = int(input('Escolha: '))
    if pergunta1 == 0:
        print(' - - SUAS INFORMAÇÕES - - ')
        print(f'''
        Nome: {nome}
        Saldo: {saldo}
        Idade: {idade}
        ''')
    elif pergunta1 == 1:
        print(' - - DEPOSITAR - - ')
        dep = float(input('Quanto depositar: R$'))
        saldo += dep
    elif pergunta1 == 2:
        print(' - - TRANSFERIR - - ')
        tran = float(input('Quantidade que quer transferir: '))
        pessoa = str(input('Nome da pessoa: '))
        lista_pessoas = []
        lista_pessoas.append(pessoa,tran)
        print('TRANSFERIDO COM SUCESSO!')
    elif pergunta1 == 3:
        estado = 'não logado'
    else:
        print('Inválido')