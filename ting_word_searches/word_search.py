def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        ocorrencias = []
        lines = instance.search(i)["linhas_do_arquivo"]
        name = instance.search(i)["nome_do_arquivo"]
        for j in range(len(lines)):
            if word in lines[j].lower():
                ocorrencias.append(
                    {"linha": j + 1}
                )
        if ocorrencias:
            result.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": ocorrencias,
                }
            )
    return result


def search_by_word(word, instance):
    result = []
    for i in range(len(instance)):
        ocorrencias = []
        lines = instance.search(i)["linhas_do_arquivo"]
        name = instance.search(i)["nome_do_arquivo"]
        for j in range(len(lines)):
            if word in lines[j].lower():
                ocorrencias.append(
                    {"linha": j + 1, "conteudo": lines[j]}
                )
        if ocorrencias:
            result.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": ocorrencias,
                }
            )
    return result
