import math

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
                   
=========================================================================================================

    Sabemos como calcular a hipotenusa de um triângulo retângulo!
    mas que tal calcular qualquer lado do triângulo retângulo? 
               
                  _____b______
                  \        |_|
                   \         |
                    \        |
    PYTHAGOREAN      \       |
      FORMULA       c \      |a
                       \     |
     c² = b² + a²       \    |
                         \   |
                          \  |
                           \ |
                            \|
                  
    Não se preocupe, o Python calcula para você...
    siga as instruções:
  
      """)
choice = (input("Qual lado a ser calculado? (a, b ou c): "))
if choice == "c":
    b = float(input("inserir o valor do lado b: "))
    a = float(input("inserir o valor do lado a: "))
    c = math.sqrt(a**2 + b**2)

    print(f"""      
=========================================================================================================
             
                          ____{b}____
                          \        |_|
                           \         |
                            \        |
         PYTHAGOREAN         \       |
           FORMULA      {c:.1f}   \      |   {a}
                               \     |
          c² = b² + a²          \    |
                                 \   |
                                  \  |
                                   \ |
                                    \|
                                    
=========================================================================================================
                                    
            """)

elif choice == "b":
    a = float(input("inserir valor do lado a: "))
    c = float(input("inserir valor do lado c: "))
    b = math.sqrt(a**2 + c**2)

    print(f"""
=========================================================================================================
                   
                          ____{b}____
                          \        |_|
                           \         |
                            \        |
         PYTHAGOREAN         \       |
           FORMULA       {c}  \      |{a}
                               \     |
          c² = b² + a²          \    |
                                 \   |
                                  \  |
                                   \ |
                                    \|
                                    
=========================================================================================================
                                    
       """)

elif choice == "a":
    c = float(input("inserir valor do lado c: "))
    b = float(input("inserir valor do lado b: "))
    a = math.sqrt(c**2 + b**2)

    print(f"""
=========================================================================================================
                   
                          ____{b}____
                          \        |_|
                           \         |
                            \        |
         PYTHAGOREAN         \       |
           FORMULA       {c}  \      |{a}
                               \     |
          c² = b² + a²          \    |
                                 \   |
                                  \  |
                                   \ |
                                    \|
                                    
=========================================================================================================
                                    
       """)
else:
    print("Invalid Input!")