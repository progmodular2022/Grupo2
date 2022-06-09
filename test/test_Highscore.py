import sys
path_to_module = "./src/"
sys.path.append(path_to_module)
import Highscore

def test_insereScore():
    arquivoCr = open("Score_test_insere_Highscore.txt", "w")
    arquivoCr.close()
    lista_usuarios = []
    for i in range(1026):
        nomeUser = "usuario" + str(i)
        pontuacaoUser = str(1026 - i)
        if i < 1024:
            assert Highscore.insereScore("test_insere_Highscore", nomeUser, pontuacaoUser) == 1
        else:
            assert Highscore.insereScore("test_insere_Highscore", nomeUser, pontuacaoUser) == -1
        lista_usuarios.append([str(1 + i), nomeUser, pontuacaoUser])
    assert Highscore.insereScore("test_insere_Highscore", "usuario-1", "1") == -1
    assert Highscore.insereScore("test_insere_Highscore", "usuario500", "521") == -1
    lista_arquivo = []
    with open("Score_test_insere_Highscore.txt", "r") as arquivoInsere:
        for linha in arquivoInsere:
            dadosScore = linha.strip().split(" ")
            lista_arquivo.append(dadosScore)
    assert lista_arquivo == lista_usuarios[:-2]
    assert lista_arquivo != lista_usuarios
    assert Highscore.insereScore("test_insere_Highscore", "usuario500", "1026") == 1
    lista_arquivo = []
    with open("Score_test_insere_Highscore.txt", "r") as arquivoInsere:
        for linha in arquivoInsere:
            dadosScore = linha.strip().split(" ")
            lista_arquivo.append(dadosScore)
    assert lista_arquivo[0] == ["1", "usuario500", "1026"]
    assert lista_arquivo[1] == ["2", "usuario0", "1026"]
    assert lista_arquivo[2] == ["3", "usuario1", "1025"]
    print("Testes da funcao insereScore concluido")

    
    
def test_buscaScore():
    arquivoCr = open("Score_test_busca_Highscore.txt", "w")
    arquivoCr.close()
    lista_usuarios = []
    for i in range(1026):
        nomeUser = "usuario" + str(i)
        pontuacaoUser = str(1026 - i)
        Highscore.insereScore("test_busca_Highscore", nomeUser, pontuacaoUser)
        lista_usuarios.append([str(1 + i), nomeUser, pontuacaoUser])
    for j in range(1026):
        if j >= 1024:
            assert Highscore.buscaScore("test_busca_Highscore", "usuario" + str(j)) == []
        else:
            assert Highscore.buscaScore("test_busca_Highscore", "usuario" + str(j)) == lista_usuarios[j]
        assert Highscore.buscaScore("test_busca_Highscore", "usuario-1") == []
    print("Teste da funcao buscaScore concluido")
        


def test_removeScore():
    arquivoCr = open("Score_test_remove_Highscore.txt", "w")
    arquivoCr.close()
    for i in range(1024):
        nomeUser = "usuario" + str(i)
        pontuacaoUser = str(i)
        Highscore.insereScore("test_remove_Highscore", nomeUser, pontuacaoUser)
    assert Highscore.removeScore("test_remove_Highscore", "usuario-1") == -1
    assert Highscore.removeScore("test_remove_Highscore", "usuario1023") == 1
    assert Highscore.removeScore("test_remove_Highscore", "usuario1021") == 1
    lista_arquivo = []
    with open("Score_test_remove_Highscore.txt", "r") as arquivoRemove:
        for linha in arquivoRemove:
            dadosScore = linha.strip().split(" ")
            lista_arquivo.append(dadosScore)
    assert lista_arquivo[0] != ["1", "usuario1023", "1023"]
    assert lista_arquivo[0] == ["1", "usuario1022", "1022"]
    assert lista_arquivo[2] != ["3", "usuario1020", "1020"]
    assert lista_arquivo[1] == ["2", "usuario1020", "1020"]
    assert len(lista_arquivo) == 1022
    print("Testes da funcao removeScore concluido")


def test_top10():
    arquivoCr = open("Score_test_top10_Highscore.txt", "w")
    arquivoCr.close()
    assert Highscore.top10("test_top10_Highscore") == []
    lista_usuarios = []
    for i in range(8):
        nomeUser = "usuario" + str(i)
        pontuacaoUser = str(8 - i)
        assert Highscore.insereScore("test_top10_Highscore", nomeUser, pontuacaoUser) == 1
        lista_usuarios.append([str(1 + i), nomeUser, pontuacaoUser])
    assert Highscore.top10("test_top10_Highscore") == lista_usuarios
    assert len(Highscore.top10("test_top10_Highscore")) == 8
    lista_user2 = []
    for i in range(15):
        nomeUser = "usuario" + str(i)
        pontuacaoUser = str(15 - i)
        assert Highscore.insereScore("test_top10_Highscore", nomeUser, pontuacaoUser) == 1
        lista_user2.append([str(1 + i), nomeUser, pontuacaoUser])
    assert Highscore.top10("test_top10_Highscore") == lista_user2[:-5]
    print("Testes da funcao top10 concluido")




test_insereScore()
test_buscaScore()
test_removeScore()
test_top10()
