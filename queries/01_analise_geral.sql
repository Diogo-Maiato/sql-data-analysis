-- Total de vendas e quantidade de produtos vendidos
SELECT COUNT(*), SUM(quantidade) FROM vendas;
-- Preço médio dos produtos
SELECT AVG(preco) FROM produtos;
-- Produto mais caro
SELECT nome_produto, preco FROM produtos ORDER by preco DESC LIMIT 1;