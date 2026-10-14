-- Quantidade total de unidades vendidas por produto
SELECT produtos.nome_produto, SUM(vendas.quantidade) 
FROM vendas 
INNER JOIN produtos 
ON vendas.id_produto = produtos.id_produto 
GROUP BY produtos.id_produto 
ORDER BY SUM(vendas.quantidade) DESC;

-- Faturaçao total por produto
SELECT produtos.nome_produto, SUM(produtos.preco * vendas.quantidade) 
FROM vendas 
INNER JOIN produtos 
ON vendas.id_produto = produtos.id_produto 
GROUP BY produtos.id_produto 
ORDER BY SUM(produtos.preco * vendas.quantidade) DESC;