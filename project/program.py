print("\n\
Olá! Você já parou pra pensar como seria sua qualidade de vida se não tivesse vícios?\n\
O tabagismo é um vício que traz uma série de riscos para sua saúde física e mental, \n\
além de custar muito caro para seu corpo e seu bolso. Pensando nisso, resolvemos mostrar\n\
um pouco do impacto que o cigarro tem trazido à sua vida. Para saber mais, basta responder\n\
a esta breve pesquisa:\n")

tempoConsumo = int(input("Há quantos anos você fuma?\nInsira um numero inteiro (Ex.: 10):\n"));
valorMaco = float(input("\nQual o valor atual do maço de cigarros? (Ex.: 10.50):\n").replace(",","."));
mediaDiariaMaco = float(input("\nQual a média de maços que você fuma por dia? (Ex.: 0.5 = meio maço):\n").replace(",","."))

valorTotal = (tempoConsumo*365) * valorMaco * mediaDiariaMaco

if(valorTotal < 20000.00):
    print(f"\nCom o valor R$ {valorTotal:.2f}, você poderia ter dado entrada em um carro.")
elif(valorTotal >= 20000.00 and valorTotal <= 50000.00):
    print(f"\nCom o valor R$ {valorTotal:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"\nCom o valor R$ {valorTotal:.2f}, você poderia ter comprado um carro zero.")

print("Esse é o impacto financeiro do cigarro durante sua vida! Vale a pena repensar, não é mesmo?")