# Repositório para testes automatizados em python usando github actions

Baseado em na template de [programmingwithalex](https://github.com/programmingwithalex)
Vindo seguinte vídeo [YouTube video](https://www.youtube.com/watch?v=rY-igT2N8zU&list=PL0dOL8Z7pG3J6t1pqRQiNarBGY-ZnIJcq&index=2).

## Descrição
Repositório para integração contínua através de testes automatizados em Python

O linting is é feito usando um GitHub Action customizado [`pylinters`](https://github.com/marketplace/actions/pylinters) escrito por programmingwithalex. 
Os testes são feito pelo pytest.

## Conteúdo

* Arquivos `main.py` e `test_main.py` que servem como exemplo para como rodar os testes automatizados
* Diretório `tests/` contém as várias runs de `pytest` que serão rodadas, uma para cada arquivo `.py` que será testado
* `requirements.txt` que contém os packages necessários para a integração contínua
