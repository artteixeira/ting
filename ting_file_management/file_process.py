from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    lines =  txt_importer(path_file)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(result)
    print(result)


def remove(instance):
    if len(instance) <= 0:
        print('Não há elementos')
        return
    
    removed = instance.dequeue()
    print(f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso\n')


def file_metadata(instance, position):
    if len(instance) <= position:
        sys.stderr.write('Posição inválida\n')
        return

    print(instance.search(position))