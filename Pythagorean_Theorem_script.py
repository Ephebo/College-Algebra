import math

# Imprime o cabeçalho
print("""
           
              ██████╗ ██╗   ██╗████████╗██╗  ██╗ █████╗  ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ███╗   ██╗    
              ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗████╗  ██║    
              ██████╔╝ ╚████╔╝    ██║   ███████║███████║██║  ███╗██║   ██║██████╔╝█████╗  ███████║██╔██╗ ██║    
              ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██╔══██║██║   ██║██║   ██║██╔══██╗██╔══╝  ██╔══██║██║╚██╗██║    
              ██║        ██║      ██║   ██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██║███████╗██║  ██║██║ ╚████║    
              ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    
                                                                                                  
                              ████████╗██╗  ██╗███████╗ ██████╗ ██████╗ ███████╗███╗   ███╗                     
                              ╚══██╔══╝██║  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║                     
                                 ██║   ███████║█████╗  ██║   ██║██████╔╝█████╗  ██╔████╔██║                     
                                 ██║   ██╔══██║██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╔╝██║                     
                                 ██║   ██║  ██║███████╗╚██████╔╝██║  ██║███████╗██║ ╚═╝ ██║                     
                                 ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝      
                                   
                                            Automação do Teorema de Pitágoras
      =========================================================================================================                     
                                                      _____b______
                                                      \        |_|
                                                       \         |
                                                        \        |
                                           PYTHAGOREAN   \       |
                                             FORMULA    c \      |a
                                                           \     |
                                          c² = b² + a²      \    |
                                                             \   |
                                                              \  |
                                                               \ |
                                                                \|
                                            
  Siga as instruções:
      """)

# Solicita ao usuário que escolha o lado a ser calculado
choice = (input("  Qual lado a ser calculado? (a, b ou c): "))
if choice == "c":
    # Se o usuário escolher calcular o lado c
    b = float(input("  inserir o valor do lado b: "))
    a = float(input("  inserir o valor do lado a: "))
    c = math.sqrt(a**2 + b**2)  # Aplica a fórmula de Pitágoras para calcular o lado c
    # Imprime o resultado
    print(f"""      
      =========================================================================================================
             
                                                      ____{b:.2f}____
                                                      \        |_|
                                                       \         |
                                                        \        |
                                     PYTHAGOREAN         \       |
                                       FORMULA      {c:.2f}  \      | {a:.2f}
                                                           \     |
                                      c² = b² + a²          \    |
                                                             \   |
                                                              \  |
                                                               \ |
                                                                \|
                                    
      =========================================================================================================
                                    
            """)
# Se o usuário escolher calcular o lado b
elif choice == "b":
    a = float(input("  inserir valor do lado a: "))
    c = float(input("  inserir valor do lado c: "))
    b = math.sqrt(a**2 + c**2) # Aplica a fórmula de Pitágoras para calcular o lado b
 
    # Imprime o resultado
    print(f"""
      =========================================================================================================
                   
                                                      ____{b:.2f}____
                                                      \        |_|
                                                       \         |
                                                        \        |
                                     PYTHAGOREAN         \       |
                                       FORMULA      {c:.2f}  \      | {a:.2f}
                                                           \     |
                                      c² = b² + a²          \    |
                                                             \   |
                                                              \  |
                                                               \ |
                                                                \|
                                    
      =========================================================================================================
                                    
       """)

elif choice == "a":
    # Se o usuário escolher calcular o lado a
    c = float(input("  inserir valor do lado c: "))
    b = float(input("  inserir valor do lado b: "))
    a = math.sqrt(c**2 + b**2) # Aplica a fórmula de Pitágoras para calcular o lado a

    # Imprime o resultado
    print(f"""
      =========================================================================================================
                   
                                                      ____{b:.2f}____
                                                      \        |_|
                                                       \         |
                                                        \        |
                                     PYTHAGOREAN         \       |
                                       FORMULA      {c:.2f}  \      | {a:.2f}
                                                           \     |
                                      c² = b² + a²          \    |
                                                             \   |
                                                              \  |
                                                               \ |
                                                                \|
                                    
      =========================================================================================================
                                    
       """)
    
else:
    # Se o usuário digitar uma escolha inválida
    print("  Invalid Input!")
# Aguarda a entrada do usuário para sair do programa
print(input("  Aperte 'enter' para sair..." ))
