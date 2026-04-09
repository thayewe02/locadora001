import tkinter as tk

#FASE 1: VARIAVEL______________________________
filmes = []

#FASE 2: MENU_______________________________

def menu ():
    print ('\nLocadora Enjoy\n'
           '1 - Cadastrar Usuario\n'
           '2 - Cadastrar Filme\n'
           '3 - Listar\n'
           '4 - Alugar \n'
           '5 - Devolver\n'
           '6 - Excluir item\n'
           '7 - Sair\n')

#FASE 3: CADASTRAR USUARIO___________________
def usuario ():
    nome = input ('Digite o nome do usuario: ').title()
    sobrenome = input ('Digite o sobrenome: ').title()
    email = input ('Digite seu email: ').lower().replace(' ','')
    print ('\nUsuario cadastrado com sucesso')
    print ('O nome e sobrenome do usuario é', nome,sobrenome)
    print (f'Email {email}')


#FASE 4: CADASTRAR FILME________________________
def cadastro ():
    nome_do_filme = input('Digite o nome do Filme: ').title()
    if nome_do_filme == '':
        print('Digite um nome Valido')
        return

    print  ('Tipos Disponiveis: \n'
          '1 - Drama\n'
          '2 - Ação\n'
          '3 - Aventura\n'
          '4 - Terror\n'
          '5 - Romance\n'
          '6 - Comedia\n'
          '7 - Suspense\n')
    tipo = input ('Digite o tipo do filme: ')

    match tipo:
        case '1': tipo = 'drama'
        case '2': tipo = 'açao'
        case '3': tipo = 'aventura'
        case '4': tipo = 'terror'
        case '5': tipo = 'romance'
        case '6': tipo = 'comedia'
        case '7': tipo = 'suspense'
        case _ :
            print ('Tipo Invalido')
            return
    filme = {'Nome': nome_do_filme,
              'Tipo': tipo }
    filmes.append(filme)
    print ('Filme Cadastrado com sucesso!')

#FASE 5: LISTAR FILMES__________________
def listar():
    if not filmes:
        print ('Nenhum filme cadastrado.')
        return
    print ('\n Filmes cadastrados\n')
    for i, filme in enumerate(filmes):
        print (f"{i + 1} - Nome: {filme['Nome']}|\n Tipo: {filme['Tipo']}")


#FASE 6: Alugar________________________

def alugar ():
    if not filmes:
        print ('Nenhum filme cadastrado.')
        return

    print ('\nFilmes Cadastrados')
    for i, filme in enumerate (filmes):
        print (f"{i + 1} - Nome: {filme['Nome']}| \n Tipo: {filme['Tipo']}")
    num_filme_alugar = int (input ('Digite o numero do filme que deseja alugar: '))
    print ('\n Filme Alugado com Sucesso')


#FASE 7: Devolver_____________________
def devolver():
    if not filmes:
        print ('Nenhum filme cadastrado.')
        return
    print('\nFilmes Cadastrados')
    for i, filme in enumerate(filmes):
        print(f"{i + 1} - Nome: {filme['Nome']} |\n Tipo: {filme['Tipo']}")
    devolver_filme = int (input ('Digite o numero do filme que deseja devolver: '))
    print ('\n O Filme foi Devolvido com Sucesso')


#FASE 8: EXCLUIR_____________________
def excluir ():
    if not filmes:
        print ('Nenhum filme cadastrado.')
        return
    print ('\nFilmes Cadastrados')
    for i, filme in enumerate(filmes):
        print(f"{i + 1} - Nome: {filme['Nome']}|\n Tipo: {filme['Tipo']}")
    excluir_item = int (input ('Digite o numero do filme que deseja excluir: '))
    filmes.pop(excluir_item-1)
    print ('\n O filme foi removido com sucesso')


#FASE 9: SAIR_____________________
def sair():
    saida = input ('Deseja sair? Digite (S/N)').strip().upper()
    if 'S' in saida :
        print ('Saindo....')

        import time
        time.sleep(3)
        print ('Programa finalizado com sucesso!!!!')
        return True
    else:
        print ('Retornando ao menu...')
        return False


#FASE 11: EXECUTAR SISTEMA _____________________
def sistema():
    while True :
        menu()
        opcao = input ('Para prosseguir Selecione sua opcao: ').strip()

        match opcao :
            case '1':
                usuario()
            case '2':
                cadastro()
            case '3':
                listar()
            case '4' :
                alugar()
            case '5':
                devolver()
            case '6':
                excluir()
            case '7':
                sair()
                break
            case _ :
                print ('Opcao Invalida..\n')


janela = tk.Tk()
janela.title("Locadora Enjoy")
janela.geometry("300x300")


botao0 = tk.Button(janela, text="Menu", command=menu)
botao0.pack()

botao1 = tk.Button(janela, text="Cadastrar Usuario", command=usuario)
botao1.pack()

botao2 = tk.Button(janela, text="Cadastrar Filme", command=cadastro)
botao2.pack()

botao3 = tk.Button(janela, text="Listar Filmes", command=listar)
botao3.pack()

botao4 = tk.Button(janela, text="Alugar Filmes", command=alugar)
botao4.pack()

botao5 = tk.Button(janela, text="Devolver Filmes", command=devolver)
botao5.pack()

botao6 = tk.Button(janela, text="Excluir Filmes", command=excluir)
botao6.pack()

botao7 = tk.Button(janela, text= 'Sair', command=sair)
botao7.pack()

janela.mainloop()