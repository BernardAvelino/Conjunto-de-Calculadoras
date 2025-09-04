print("----------------------------------")
print("-----Calculadora de Descontos-----")
print("----------------------------------")
print("")
print("Atento as orientações: O desconto só pode ser usado com produtos acima de R$100,00")

def descontoq(valorp, desconto):
    conta = valorp - (valorp * desconto / 100)
    return conta

valor = float(input("Digite o valor do seu produto: "))
descon = float(input("Digite o valor do desconto do produto: "))

if valor > 99:
    resultado = descontoq(valor, descon)
    print(f"O valor final do seu produto com o desconto é de R${resultado:.2f}")
else:
    print(f"O seu produto não tem o valor necesssário para o desconto. Valor final R${valor}")
    

    