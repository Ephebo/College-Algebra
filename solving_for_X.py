# Coloque 0 para a icógnita. 

def solving_for_x(n1,d1,n2,d2):
    if d2 == 0:
      answer = (d1*n2)/n1
      return answer
    elif n2 == 0:
      answer = (n1*d2)/d1
      return answer
    elif d1 == 0:
      answer = (d2*n1)/n2
      return answer
    elif n1 == 0:
      answer = (d1*n2)/d2
      return answer


  
print("""
    Bem vindo ao Solving for x

            ██╗  ██╗
            ╚██╗██╔╝
             ╚███╔╝ 
             ██╔██╗ 
            ██╔╝ ██╗
            ╚═╝  ╚═╝       
            
          _n1_ = _n2_
           d1     d2
           
    Obs: Coloque 0 para a icógnita.
      """)

n1 = int(input("digite o valor de n1: "))
n2 = int(input("digite o valor de n2: "))
d1 = int(input("digite o valor de d1: "))
d2 = int(input("digite o valor de d2: "))

result = solving_for_x(n1,d1,n2,d2)

if n2 == 0:
      print(f"""
      
      _{n1}_ = _X_
       {d1}     {d2}
       
        x = {result:.0f}
      
      """)

elif d2 == 0:
      print(f"""
      
      _{n1}_ = _{n2}_
       {d1}     X
       
      x = {result:.0f}
      
      """)
      
elif n1 == 0:
      print(f"""
      
      _X_ = _{n2}_
       {d1}     {d2}
       
      x = {result:.0f}
      
      """)
else:
      print(f"""
      
      _{n1}_ = _{n2}_
       X     {d2}
       
      x = {result:.0f}
      
      """)
print(input('aperte: "enter" para sair.....'))
      