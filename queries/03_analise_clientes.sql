-- Top 5 clientes por faturação
SELECT clientes.nome, SUM(produtos.preco * vendas.quantidade) 
FROM Clientes 
INNER JOIN vendas
ON vendas.id_cliente = clientes.id_cliente 
INNER JOIN Produtos 
ON  vendas.id_produto = produtos.id_produto
GROUP BY clientes.id_cliente 
ORDER BY SUM(produtos.preco * vendas.quantidade) DESC LIMIT 5;

-- Clientes que nunca fizeram compras
SELECT clientes.nome 
FROM clientes
LEFT JOIN vendas
ON vendas.id_cliente = clientes.id_cliente
WHERE vendas.id_produto IS NULL;