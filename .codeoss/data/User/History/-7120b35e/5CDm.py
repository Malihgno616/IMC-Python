#Cálculo IMC

print("Bem vindo ao cálculo de IMC")
print("\nConfira já o seu!!!")

def calculoIMC (A, B):
    IMC = A / (B ** 2)
    return IMC    

def ideal_ou_nao_ideal(IMC):
    if IMC < 16:
        return print("\nMagreza Grau III")
    elif IMC == 16 and IMC <= 16.9:
        return print("\nMagreza Grau II")
    elif IMC >=17 and IMC <= 18.4:
        return print("\nMagreza Grau I")         



peso = float(input("Quantos KG você pesa? "))
print(peso)

altura = float(input("Qual é a sua altura em metros? "))
print(altura)

numeroIMC = calculoIMC(peso, altura)

print(round(numeroIMC, 4))

ideal_ou_nao_ideal(numeroIMC)

