import json
import os
import platform


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        return []


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


def limpar_tela():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def limpar_dados(tarefas, caminho_arquivo):
    tarefas.clear()
    salvar(tarefas, caminho_arquivo)
    print('Todas as tarefas foram removidas.')
    listar(tarefas)


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler(CAMINHO_ARQUIVO)
tarefas_refazer = []

comandos = {
    '1': lambda: listar(tarefas),
    'listar': lambda: listar(tarefas),
    '2': lambda: (desfazer(tarefas, tarefas_refazer), salvar(tarefas, CAMINHO_ARQUIVO)),
    'desfazer': lambda: (desfazer(tarefas, tarefas_refazer), salvar(tarefas, CAMINHO_ARQUIVO)),
    '3': lambda: (refazer(tarefas, tarefas_refazer), salvar(tarefas, CAMINHO_ARQUIVO)),
    'refazer': lambda: (refazer(tarefas, tarefas_refazer), salvar(tarefas, CAMINHO_ARQUIVO)),
    '4': lambda: limpar_tela(),
    'clear': lambda: limpar_tela(),
    '5': lambda: limpar_dados(tarefas, CAMINHO_ARQUIVO),
    'limpar': lambda: limpar_dados(tarefas, CAMINHO_ARQUIVO),
    'resetar': lambda: limpar_dados(tarefas, CAMINHO_ARQUIVO)
}


def menu():
    print('Comandos:')
    print('[1] listar')
    print('[2] desfazer')
    print('[3] refazer')
    print('[4] clear')
    print('[5] limpar todas as tarefas')
    print('Digite a tarefa para adicionar')
    print()


while True:
    menu()
    comando = input('Digite um comando ou tarefa: ').strip().lower()

    if comando in comandos:
        comandos[comando]()
    else:
        adicionar(comando, tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
        listar(tarefas)
