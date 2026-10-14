-- Faturaçao mensal 

SELECT strftime('%Y-%m',vendas.data_venda) AS mes , SUM(produtos.preco * vendas.quantidade)
FROM vendas
INNER JOIN Produtos
ON vendas.id_produto = produtos.id_produto
GROUP BY mes
ORDER BY SUM(produtos.preco * vendas.quantidade) DESC ;