def calculadora_juros(principal, juros, anos):
    montante = principal + (principal * juros * anos / 100)
    return montante

valor = float(input("Digite o valor principal: "))
taxa = float(input("Digite a procentagem da taxa: "))
tempo = int(input("Digite quantos anos: "))

resultado = calculadora_juros(valor, taxa, tempo)

print(f"O valor final com a taxa de {taxa:.2f}% em {tempo} anos, é de R${resultado:.2f}")
