aparelho = ""
potencia = 0
horas = 0

def calcCons(pot, hr):
    return (pot * hr * 30) / 1000

def calcValor(cons):
    return float(cons / 0.72)

def main():
    print("Bem-vindo à Calculadora de Consumo de Energia Elétrica.")
    
    global aparelho, potencia, horas
    aparelho = input("\n\nInforme o aparelho a ser calculado: ")
    potencia = float(input("\nInforme a potência do aparelho em Watts (W): "))
    horas = int(input("\nInforme a quantidade diária de horas que o aparelho é usado: "))
    
    consumo = calcCons(potencia, horas)
    preco = calcValor(consumo)
    
    print(f"\nAparelho: {aparelho}\nConsumo médio mensal: {consumo:.2f} kWh\nValor médio: R${preco:.2f}")

main()
