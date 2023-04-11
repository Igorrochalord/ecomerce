from django.shortcuts import render
import pandas as pd
from time import sleep
from tqdm import tqdm

def index(request):
    if request.method == 'POST':
        codigo = []
        nome_produto = []
        preco = []
        quantidades = []
        categorias = []

        passando = int(request.POST['codigo_produto'])
        nomep = request.POST['nome_produto']
        preci = float(request.POST['preco'])
        quantidade = int(request.POST['quantidade'])
        categoria = request.POST['categoria']

        codigo.append(passando)
        nome_produto.append(nomep)
        preco.append(preci)
        quantidades.append(quantidade)
        categorias.append(categoria)

        dados = {'codigo_produto': codigo,
                 'Nome do Produto': nome_produto,
                 'Preço': preco,
                 'Quantidade em Estoque': quantidades,
                 'Categoria': categorias}

        mercado = pd.DataFrame(dados)

        for i in range(len(mercado)):
            if mercado.loc[i, 'Quantidade em Estoque'] <= 10:
                estoque_baixo = f"Atenção! O produto {mercado.loc[i, 'Nome do Produto']} está acabando. A quantidade em estoque é de {mercado.loc[i, 'Quantidade em Estoque']} unidades."
            else:
                estoque_baixo = ""

        context = {
            'mercado': mercado.to_html(index=False),
            'estoque_baixo': estoque_baixo
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')
