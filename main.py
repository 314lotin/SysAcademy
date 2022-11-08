import helpers
from time import sleep

lista_alunos = helpers.arqToVar()


## Imprime o menu
def menu():
    helpers.clearScreen()
    print(40 * "=" +
        """\nSysAcademy

        1. Cadastrar novo aluno
        2. Imprimir lista de alunos
        3. Buscar aluno por ID
        4. Filtrar alunos com IMC > 30
        5. Salvar dados e sair
        \n\r""" +
        40 * "=" +
        "\nOpção: ", end='')
    return str(input())
##


## Cadastrar aluno
def cadastroAluno():
    confirma = "N"


    ## Checa se o usuário não clicou por acidente
    helpers.clearScreen()
    print(40 * "=" + "\nCadastrar Aluno" + "\nProsseguir S/N: ", end = "")
    if input() not in ["", "S", "s"]:
        return None


    while confirma not in ["", "S", "s"]:
        helpers.clearScreen()
        print(40 * "=" + "\nCadastrar Aluno")


        ## Dicionario Aluno
        aluno = {
            "Nome":"",
            "Sexo":"",
            "Telefone":"",
            "Peso":float(),
            "Altura":float(),
            "Mensalidade":float(),
            "ID":""
        }
        ##


        for key in aluno:
            while aluno[key] == "" or aluno[key] == 0.0:
                try:
                    if aluno[key] == 0.0:
                        aluno[key] = float(input(f"{key}: "))
                    else:
                        aluno[key] = ''.join(filter(str.isalnum, str(input(f"{key}: ")).strip()))
                except:
                    print(f"Erro: Digite {key} novamente")


        ## Confirma
        confirma = input(40 * "=" + "\nOs dados estão corretos S/N: ")
        ##

    helpers.addAluno(aluno, lista_alunos)
##
 

## Função para ler os alunos
def imprimirAluno():
    helpers.clearScreen()
    if len(lista_alunos) == 0:
        print("\n" + "\033[31m" + "***Nenhum aluno cadastrado ainda***" + "\033[0;0m")
    else:
        for aluno in lista_alunos:
            print(f"{aluno['Nome']:<40}::  {aluno['ID']}")
    
    print("\n\n" + 40 * "=" + "\nAperte Return para voltar...")
    input()
##


## Buscar aluno por ID
def buscaPorID():
    helpers.clearScreen()
    print(40 * "=" + "\n")

    id_aluno = ''.join(filter(str.isalnum, input("Insira o ID: ")))

    achou_aluno = False
    for aluno in lista_alunos:
        if aluno["ID"] == id_aluno:
            achou_aluno = True
            print(40 * "=")
            for key in aluno:
                print(f"{key:<15}: {str(aluno[key])}")
    if not achou_aluno:
        print("\n" + "\033[31m" + "***Aluno não encontrado***" + "\033[0;0m")
    
    print("\n\n" + 40 * "=" + "\nAperte Return para voltar...")
    input()
##


## IMC > 30
def imc30():
    helpers.clearScreen()
    print(40 * "=" + "\n")

    imcmaior = False
    for aluno in lista_alunos:
        if aluno["Peso"] / (aluno["Altura"] ** 2) > 30:
            imcmaior = True
            print(40 * "=")
            for key in aluno:
                print(f"{key:<15}: {str(aluno[key])}")
    if not imcmaior:
        print("\n" + "\033[31m" + "***Nenhum aluno com IMC maior que 30***" + "\033[0;0m")

    print("\n\n" + 40 * "=" + "\nAperte Return para voltar...")
    input()
##


## salvar os dados e sair
def salvarESair():
    helpers.escreveJSON(lista_alunos)
    exit()
##




## Função principal
def main():
    while True:
        opcao = menu()
        if opcao == "1":
            cadastroAluno()
        elif opcao == "2":
            imprimirAluno()
        elif opcao == "3":
            buscaPorID()
        elif opcao == "4":
            imc30()
        elif opcao == "5":
            salvarESair()
        else:
            print("\n" + "\033[31m" + "***Opção inválida***" + "\033[0;0m")
            sleep(0.6)


## Impedir que o arquivo seje executado como módulo
if __name__ == "__main__":
    main()
