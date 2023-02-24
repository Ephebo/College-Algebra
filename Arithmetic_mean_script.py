print("""
 █████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗███████╗████████╗██╗ ██████╗   
██╔══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║██╔════╝╚══██╔══╝██║██╔════╝   
███████║██████╔╝██║   ██║   ███████║██╔████╔██║█████╗     ██║   ██║██║       
██╔══██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██║██║       
██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗   ██║   ██║╚██████╗  
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝  


                ███╗   ███╗███████╗ █████╗ ███╗   ██╗
                ████╗ ████║██╔════╝██╔══██╗████╗  ██║
                ██╔████╔██║█████╗  ███████║██╔██╗ ██║
                ██║╚██╔╝██║██╔══╝  ██╔══██║██║╚██╗██║
                ██║ ╚═╝ ██║███████╗██║  ██║██║ ╚████║
                ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                
             Script para automatizar a Média Aritmética

Por favor, separar os dados com uma "," vírgula.                  
""")

# 📌 1 converter o input para float
lista_das_distâncias = input("Inserir notas: ").split(", ")
for n in range(0, len(lista_das_distâncias)):
    lista_das_distâncias[n] = float(lista_das_distâncias[n])
# converte a lista originalmente de string para int

# 📌 2 somar as distâncias
suma_das_distâncias = 0
for n in lista_das_distâncias:
    suma_das_distâncias += n

# 📌 3 contar o tamanho da lista
tamanho_da_lista = 0
for tamanho in lista_das_distâncias:
    tamanho_da_lista += 1
    
# 📌 4 Calcule a média
média_aritmética = suma_das_distâncias / tamanho_da_lista
print(f"A Média Aritmética é = {média_aritmética:.1f}")

print(input("Aperte 'enter' para sair..."))