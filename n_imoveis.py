# Inicializa a variável para contar o total de imóveis
total_imoveis = 0

# Laço para solicitar a quantidade de imóveis construídos em cada ano de 2020 a 2024
for ano in range(2020, 2025):
    quantidade_imoveis = float(input(f'Digite a quantidade de imóveis no ano {ano}: '))
    total_imoveis += quantidade_imoveis  # Incrementa o total de imóveis com a quantidade informada

# Exibe o total de imóveis construídos no período
print(f'Total de imóveis construídos: {total_imoveis} imóveis')


