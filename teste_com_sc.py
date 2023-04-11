import pandas as pd
import cv2
import pyzbar.pyzbar as pyzbar
from time import sleep
from tqdm import tqdm

# lista vazia que vai receber os dados
codigo = []
nome_produto = []
preco = []
quantidades = []
categorias = []

# entrada do usuário
user = input("Digite seu nome:")
cod = int(input("Digite seu registro:"))

def ler_codigo_de_barras(imagem):
    # conversão da imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # detecção dos códigos de barras na imagem
    codigos = pyzbar.decode(imagem_cinza)
    # iteração sobre os códigos detectados
    for codigo in codigos:
        # conversão do código para string
        codigo_decodificado = codigo.data.decode('utf-8')
        # adição do código à lista de códigos
        codigo.append(codigo_decodificado)

while True:
    # exibição do menu
    print("======= Rede Portela de Supermercado =======")
    print("1 - Cadastrar Produto")
    print("2 - Exibir Produtos em Estoque")
    print("3 - Sair")
    print("4 - Digitalizar Produto")

    # entrada da opção do usuário
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # cadastro de produto
        passando = int(input("Código do produto: "))
        nomep = input("Nome do produto: ")
        preci = float(input("Preço: "))
        quantidade = int(input("Quantidade do produto: "))
        categoria = input("Categoria do produto: ")

        codigo.append(passando)
        nome_produto.append(nomep)
        preco.append(preci)
        quantidades.append(quantidade)
        categorias.append(categoria)

        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        # exibição dos produtos em estoque
        dados = {'Código do Produto': codigo,
                 'Nome do Produto': nome_produto,
                 'Preço': preco,
                 'Quantidade em Estoque': quantidades,
                 'Categoria': categorias}

        mercado = pd.DataFrame(dados)

        for i in range(len(mercado)):
            if mercado.loc[i, 'Quantidade em Estoque'] <= 10:
                print(f"Atenção! O produto {mercado.loc[i, 'Nome do Produto']} está acabando. A quantidade em estoque é de {mercado.loc[i, 'Quantidade em Estoque']} unidades.")

        exibir_resultado = input("Deseja exibir o resultado? (s/n) ")
        if exibir_resultado == "s":
            for i in tqdm(range(100)):
                sleep(0.02)
            print(mercado)

    elif opcao == "3":
        # encerramento do programa
        print("Programa encerrado!")
        break

    elif opcao == "4":
        # digitalização do produto
        cap = cv2.VideoCapture(0)