#Cálculo IMC

print("Bem vindo ao cálculo de IMC")
print("\nConfira já o seu!!!")

def calculoIMC (A, B):
    IMC = A / (B ** 2)
    return IMC    


peso = float(input("Quantos KG você pesa? "))
print(peso)

altura = float(input("Qual é a sua altura em metros? "))
print(altura)

numeroIMC = calculoIMC(peso, altura)


print(round(numeroIMC, 3))
