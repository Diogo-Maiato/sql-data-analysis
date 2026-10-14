-- Desempenho de cada funcionario 

SELECT funcionarios.nome , SUM(produtos.preco * vendas.quantidade)
FROM funcionarios
INNER JOIN vendas 
ON vendas.id_funcionario = funcionarios.id_funcionario 
INNER JOIN Produtos 
ON  vendas.id_produto = produtos.id_produto
GROUP BY funcionarios.nome
ORDER BY SUM(produtos.preco * vendas.quantidade) DESC;