produto = input("Digite o produto que deseja comprar:")
qntProduto = float(input("Digite a quantidade de produtos que ira comprar:"))
valorUnitario = float(input("Digite o valor unitario do produto:"))
desconto = float(input("Digite a porcentagem de desconto a ser aplicada:"))
preco = qntProduto*valorUnitario
porcentagem = (desconto/100)* preco
total = preco - porcentagem
print("O produto %s terá o preço total de: %.2f"%(produto, total))
