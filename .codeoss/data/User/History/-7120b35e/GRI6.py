#Cálculo IMC

print("Bem vindo ao cálculo de IMC")
print("\nConfira já o seu!!!")

def calculoIMC (A, B):
    IMC = A / (B ** 2)
    return IMC    

def ideal_ou_nao_ideal(IMC):
    if IMC < 16:
        return print("Magreza Grau III")
    elif IMC == 16 and IMC <= 16.9:
        return print("Magreza Grau II")
    elif IMC >=17 and IMC <= 18.4:
        return print("Magreza Grau I")         
    elif IMC ==18.5 and IMC <= 24.9:
        return print("Adequado")
    elif IMC == 25 and IMC <= 29.9:
        return print("Pré Obeso")
    elif IMC == 30 and IMC <= 34.9:
        return print("Obesidade I")
    elif IMC == 34.9 and IMC <=       

peso = float(input("Quantos KG você pesa? "))
print(peso)

altura = float(input("Qual é a sua altura em metros? "))
print(altura)

numeroIMC = calculoIMC(peso, altura)

print(round(numeroIMC, 2))

ideal_ou_nao_ideal(numeroIMC)

