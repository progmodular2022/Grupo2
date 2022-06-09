
from os.path import exists


def criacaoArquivo(func):
    def inner(nomeJogo, *args, **kwargs):
        nomeArquivo = "Score_" + nomeJogo + ".txt"
        if not exists(nomeArquivo):
            criacaoArq = open(nomeArquivo, "x")
            criacaoArq.close()
        return func(nomeJogo, *args, **kwargs)
    return inner

@criacaoArquivo
def insereScore(nomeJogo, nomeUsuario, pontuacao) -> int:
    #Insere os dados da nova pontuacao no arquivo referente a nomeJogo
    #Caso o usuario ja esteja no arquivo, so insere caso a nova pontuacao seja maior que a registrada
    #Todos os parametros devem ser strings
    #No arquivo serao registrados a posicao, nomeUsuario e pontuacao
    #Tais dados ficarao separados por " "
    #O limite de dados salvos no arquivo e de 1024
    #A funcao retorna -1 caso a nova pontuacao nao seja inserida
    #A funcao retorna 1 na insercao com sucesso da pontuacao
    listaLinhas = []
    novaPosicao = 1
    contador = 1
    nomeArquivo = "Score_" + nomeJogo + ".txt"
    with open(nomeArquivo, "r") as arquivo:
        for linha in arquivo:
            contador += 1 
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                contador -= 1
                if int(pontuacao) < int(linhaScore[2]):
                    return -1
            else:
                listaLinhas.append(linhaScore)
            
            if int(linhaScore[2]) > int(pontuacao):
                novaPosicao += 1
    
    if novaPosicao > 1024:
        return -1
    if contador > 1024:
        contador = 1024
    listaLinhas.insert(novaPosicao - 1 , [str(novaPosicao), nomeUsuario, pontuacao])

    with open(nomeArquivo, "w") as arquivoSaida:
        for i in range(contador):
            arquivoSaida.write(str(i + 1) + " " + listaLinhas[i][1] + " " + listaLinhas[i][2] + "\n")
    return 1


@criacaoArquivo
def buscaScore(nomeJogo, nomeUsuario) -> list:
    #Retorna uma lista contendo a posicao, o nomeUsuario e a pontuacao referentes a busca
    #Todos os parametros devem ser strings
    #Retorna lista vazia caso o nomeUsuario nao seja encontrado no arquivo
    nomeArquivo = "Score_" + nomeJogo + ".txt"
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        for linha in arquivo:
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                return linhaScore
    return []

@criacaoArquivo
def removeScore(nomeJogo, nomeUsuario) -> int:
    #Remove os dados referentes a nomeUsuario no arquivo de nomeJogo
    #Atualiza os dados do Highscore apos a remocao
    #Todos os parametros devem ser strings
    #Retorna -1 caso o nomeUsuario nao seja encontrado no arquivo
    #Retorna 1 ao remover a pontuacao com sucesso
    contador = 0
    listaLinhas = []
    usuarioEncontrado = 0
    nomeArquivo = "Score_" + nomeJogo + ".txt"
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        for linha in arquivo:
            contador += 1 
            linhaScore = (linha.strip()).split(" ")
            if linhaScore[1] == nomeUsuario:
                usuarioEncontrado = 1
            else:
                listaLinhas.append(linhaScore)

    if usuarioEncontrado == 0:
        return -1
    else:
        with open("Score_" + nomeJogo + ".txt", "w") as arquivoSaida:
            for i in range(contador - 1):
                arquivoSaida.write(str(i + 1) + " " + listaLinhas[i][1] + " " + listaLinhas[i][2] + "\n")
    return 1
    
    
@criacaoArquivo
def top10(nomeJogo) -> list:
    #Retorna uma lista referente as 10 melhores pontuacoes salvas no arquivo de nomeJogo
    #Cada elemento da lista e uma lista contendo posicao, nome do usuario e pontuacao
    #Se o numero de pontuacoes salvas no arquivo for menor do que 10, todos os dados serao retornados na lista
    nomeArquivo = "Score_" + nomeJogo + ".txt"
    with open("Score_" + nomeJogo + ".txt", "r") as arquivo:
        listatop10 = []
        cont = 0
        for linha in arquivo:
            linhaScore = (linha.strip()).split(" ")
            if cont < 10:
                listatop10.append(linhaScore)
            else:
                break
            cont += 1
    return listatop10
