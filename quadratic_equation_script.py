"""
Tema: Equação de 2° grau
Tecnologia: Python
Objetivo: Criar um script que peça um input do usuário e calcule uma equação de 2° grau.

Aluno: Matheus Alves Dantas
Data: 24/02/2023

"""


# 📌 criar uma função que calcule as raizes

def calcular_raizes(a,b,c): 
# calculando o determinante delta:
    Δ = b**2 - 4*a*c
    
# verificando as condições
    if Δ < 0:
        return None
# se delta for menor que zero, returna None, ou seja, nada.

    elif Δ == 0:
        x = (-b/(2*a))
        return x, None
        
# x=(-b+-√Δ)/2a –› x=-b/2a
# Se delta for igual a zero, implica que a equação só tem uma única raiz
# permitindo calcular diretamente
        
    else:
        x1 = (-b+(Δ**(1/2))) /(2*a)
        x2 = (-b-(Δ**(1/2))) /(2*a)
        
# x=(-b+-√Δ)/2a
# se delta > 0, implica que tem duas raizes Reais.
        return x1,x2




print("""
      
         ██████╗ ██████╗ ██╗     ███████╗██╗  ██╗
        ██╔════╝██╔═══██╗██║     ██╔════╝╚██╗██╔╝
        ██║     ██║   ██║██║     █████╗   ╚███╔╝ 
        ██║     ██║   ██║██║     ██╔══╝   ██╔██╗ 
        ╚██████╗╚██████╔╝███████╗███████╗██╔╝ ██╗
         ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
         
        script para calcular Equação de 2° graus
                                                         
                     x=(-b+-√Δ)/2a
                     Δ = b² - 4ac
      """)   
    
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


roots = calcular_raizes(a,b,c)

if roots is None:
    print("O resultado não pertence aos reais R* ")
else:
    x1_root, x2_root = roots 
    print(f"As raizes da equação são x1 = {x1_root} e x2 = {x2_root}")
    
print(input("Pressione 'Enter' para sair..."))
