# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

def calcular_média():
    total = 0
    contador = 0
    
    while True:
        num = float(input("digite um número:"))
        if num == -1:
            break
        total += num
        contador += 1 
        
    if contador > 0:
        média = total / contador
        print (f"a média é {média}")
    else:
        print ("nenhum número foi digitado")
        
calcular_média()
        
        
        