
# 📌 criar uma função que calcule as raizes

def calcular_raizes(a,b,c): 
# calculando o determinante delta:
    Δ = b**2 - 4*a*c
    
# verificando as condições
    if Δ < 0:
        return None # Raízes complexas, o resultado não pertence aos reais
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
      
                         ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗  █████╗ ████████╗██╗ ██████╗    
                        ██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝    
                        ██║   ██║██║   ██║███████║██║  ██║██████╔╝███████║   ██║   ██║██║         
                        ██║▄▄ ██║██║   ██║██╔══██║██║  ██║██╔══██╗██╔══██║   ██║   ██║██║         
                        ╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║██║  ██║   ██║   ██║╚██████╗    
                         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝    
                                                                          
                          ███████╗ ██████╗ ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗         
                          ██╔════╝██╔═══██╗██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║         
                          █████╗  ██║   ██║██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║         
                          ██╔══╝  ██║▄▄ ██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║         
                          ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║         
                          ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝         
                                                                          
                                         Automação da Equação de 2° Graus
                                                         
                                                  x=(-b+-√Δ)/2a
                                                   Δ = b² - 4ac
      """)   
    
a = float(input("  Digite o valor de a: "))
b = float(input("  Digite o valor de b: "))
c = float(input("  Digite o valor de c: "))

# Função para calcular as raízes da equação de segundo grau
roots = calcular_raizes(a,b,c)

if roots is None: 
    print("  O resultado não pertence aos reais R* ") 
else:
    x1_root, x2_root = roots 
    print(f"  As raizes da equação são x1 = {x1_root:.2f} e x2 = {x2_root:.2f}")
    
print(input("  Pressione 'Enter' para sair..."))
