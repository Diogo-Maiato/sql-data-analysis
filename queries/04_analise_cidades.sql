-- Faturaçao por cidade

SELECT clientes.cidade, SUM(produtos.preco * vendas.quantidade)
FROM clientes
INNER JOIN vendas 
ON vendas.id_cliente = clientes.id_cliente
INNER JOIN Produtos 
ON vendas.id_produto = produtos.id_produto
GROUP BY clientes.cidade
ORDER BY SUM (produtos.preco * vendas.quantidade) DESC ;