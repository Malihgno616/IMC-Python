#Cálculo IMC

print("Bem vindo ao cálculo de IMC")
print("\nConfira já o seu!!!")

def calculoIMC (A, B):
    IMC = A / (B ** 2)
    return IMC    

def ideal_ou_nao_ideal(A):
    if A < 16:
        print("Magreza Grau III")
    elif A > 16 and A <= 17:
        print("Magreza Grau II")
    elif A       

peso = float(input("Quantos KG você pesa? "))
print(peso)

altura = float(input("Qual é a sua altura em metros? "))
print(altura)

numeroIMC = calculoIMC(peso, altura)

print(round(numeroIMC, 4))
