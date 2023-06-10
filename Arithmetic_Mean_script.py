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
                
                                            Automação de Média Aritmética

                              Obs: Por favor, separar os dados com vírgula e espaço ", "                 
""")

# 📌 Passo 1: Converter o input para float
# Solicita ao usuário que insira os dados separados por vírgula e espaço
lista_das_distâncias = input("  Inserir dados: ").split(", ")
# Converte cada elemento da lista original de string para float
for n in range(0, len(lista_das_distâncias)):
    lista_das_distâncias[n] = float(lista_das_distâncias[n])

# 📌 Passo 2: Somar as distâncias
# Inicializa a variável soma_das_distâncias como zero
suma_das_distâncias = 0
# Percorre cada elemento da lista das distâncias
for n in lista_das_distâncias:
    # Adiciona o valor do elemento à soma_das_distâncias
    suma_das_distâncias += n

# 📌 Passo 3: Contar o tamanho da lista
# Inicializa a variável tamanho_da_lista como zero
tamanho_da_lista = 0
# Percorre cada elemento da lista das distâncias
for tamanho in lista_das_distâncias:
    # Incrementa o tamanho_da_lista em 1 a cada iteração
    tamanho_da_lista += 1
    
# 📌 Passo 4: Calcule a média
# Divide a soma das distâncias pelo tamanho da lista para obter a média aritmética
média_aritmética = suma_das_distâncias / tamanho_da_lista
# Imprime a média aritmética com uma casa decimal
print(f"  A Média Aritmética é = {média_aritmética:.1f}")

# Aguarda o usuário pressionar 'enter' para sair
print(input("""
  Aperte 'enter' para sair...
            """))
