#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário deve escolher a unidade de entrada e a unidade de saída. Use float() para garantir precisão.


medidas = {("celsius","fahrenheit"):lambda celsius: celsius * 9/5 + 32,
           ("celsius","kelvin"):lambda celsius: celsius + 273.15,
           ("fahrenheit","celsius"):lambda fahrenheit: (fahrenheit - 32) * 5/9,
           ("fahrenheit","kelvin"):lambda fahrenheit: (fahrenheit - 32) * 5/9 + 273.15,
           ("kelvin","celsius"):lambda kelvin: kelvin - 273.15,
           ("kelvin","fahrenheit"):lambda kelvin: (kelvin - 273.15) * 9/5 + 32
           }

while True:
  try:
    getMedidaAtual = input("Digite a medida atual -> Celsius, Fahrenheit, Kelvin: ").lower()
    getMedidaParaConversao = input("Digite a medida para conversão -> Celsius, Fahrenheit, Kelvin: ").lower()
    getTemperatura = float(input("Digite a temperatura: "))
    if medidas.get((getMedidaAtual,getMedidaParaConversao)):
      func = medidas.get((getMedidaAtual,getMedidaParaConversao))
      print(f"Valor convertido de {getMedidaAtual.capitalize()} para {getMedidaParaConversao.capitalize()}: {func(getTemperatura)} Graus {getMedidaParaConversao.capitalize()}")
      break
    else:
      print("medida não existe")
  except ValueError:
    print("Valor inválido")
