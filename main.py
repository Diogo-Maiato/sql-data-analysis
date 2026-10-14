import sqlite3 as sql
from pathlib import Path

diretorio = Path(__file__).resolve().parent
ficheiro = sql.connect("data/empresa.db")

cursor = ficheiro.cursor()

def executar_query(nome_ficheiro):
    caminho = diretorio/ "queries" / nome_ficheiro 
    conteudo = caminho.read_text(encoding="utf-8")

    consultas = conteudo.split(";")
    resultados = []

    for consulta in consultas:
        if consulta.strip():
            cursor.execute(consulta)
            resultados.append(cursor.fetchall())

    return resultados
resultados_gerais = executar_query("01_analise_geral.sql")

total_vendas, total_produtos = resultados_gerais[0][0]
media_preco_produtos = resultados_gerais[1][0][0]
maior_preco_produto = resultados_gerais[2][0]

resultados_produtos = executar_query("02_analise_produtos.sql")

quantidade_por_produto = resultados_produtos[0]
faturacao_produto = resultados_produtos[1]

resultados_clientes = executar_query("03_analise_clientes.sql")

top_clientes = resultados_clientes[0]
cliente_sem_compras = resultados_clientes[1]

resultados_cidades = executar_query("04_analise_cidades.sql")

faturacao_cidade = resultados_cidades[0]

resultados_temporais = executar_query("05_analise_temporal.sql")

faturacao_mensal = resultados_temporais[0]

resultados_funcionarios = executar_query("06_analise_funcionarios.sql")

melhores_funcionarios = resultados_funcionarios[0]


print("\n========== ANÁLISE GERAL ==========\n")

print(f"Foram feitas {total_vendas} vendas no total. \nSendo elas um total de {total_produtos} produtos vendidos.")
print(f"Preço médio dos produtos: {media_preco_produtos:.2f} €")
print(f"O produto mais caro e {maior_preco_produto[0]} e custa {maior_preco_produto[1]:.2f} Euros.")

print("\n========== PRODUTOS MAIS VENDIDOS ==========\n")
 
for produto, quantidade in quantidade_por_produto:
    print(f"{produto} -> {quantidade} unidades.")

print("\n========== FATURAÇÃO POR PRODUTO ==========\n")   

for produto, faturacao in faturacao_produto:
    print(f"{produto} -> {faturacao:.2f} Euros.")

print("\n========== TOP 5 CLIENTES POR FATURAÇÃO ==========\n")   

for nome_cliente, gasto_cliente in top_clientes:
    print(f"{nome_cliente} -> {gasto_cliente:.2f} Euros")

print("\n========== CLIENTES SEM GASTOS ==========\n")   

for (nome,) in cliente_sem_compras:
    print(f'{nome} -> sem compras')

print("\n========== FATURACAO POR CIDADE ==========\n")   

for cidade, gasto_cidade in faturacao_cidade:
     print(f"{cidade} -> {gasto_cidade:.2f} Euros ")

print("\n========== FATURAÇÃO MENSAL ==========\n")   

for mes, gasto_mes in faturacao_mensal:
    print(f"{mes} -> {gasto_mes:.2f} Euros.")

print("\n========== VENDAS DOS FUNCIONARIOS ==========\n")   

for nome_funcionario, venda_funcionario in melhores_funcionarios:
    print(f"{nome_funcionario} teve uma faturacao de {venda_funcionario:.2f} Euros")

ficheiro.close()