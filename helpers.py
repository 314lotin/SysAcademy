import sys, os, json


## Limpa tela
def clearScreen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
##


## Função para escrever o aluno no arquivo json
def escreveJSON(aluno_lista):
    # com 'with open' o arquivo se fecha sozinho após as operações
    with open("listaalunos.json", "w", encoding="utf-8") as arq:
        json.dump(aluno_lista, arq, indent = 4, sort_keys = True, separators=(',', ': '), ensure_ascii = False)
##


## Tenta abrir o arquivo e retornar uma varivel lista, onde vai ser salvo os alunos em forma de dicionário
def arqToVar():
    try:
        with open("listaalunos.json", encoding="utf-8") as arq:
            ret = json.load(arq)

    # Erro caso não exista o arquivo
    except OSError:
        with open("listaalunos.json", "w+", encoding="utf-8") as arq:
            pass
        ret = []

    # Erro caso o arquivo esteja vazio
    except:
        ret = []
    
    return ret
##


## Adiciona o aluno a lista de alunos
def addAluno(aluno, var):
    var.append(aluno)
##

