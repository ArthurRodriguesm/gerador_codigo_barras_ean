from random import randint

def code_ean_generator():
    ean_list = ['7','9', '0']

    for i in range(5): # Gerando dígitos do fabricante
        ean_list.append(str(randint(0,9)))
        
    for i in range(4): # Gerando digitos do produto
            ean_list.append(str(randint(0,4)))         

    transform_int_numbers(ean_list)

def transform_int_numbers(list):
    numeros_inteiros = [int(numero) for numero in list]
    print(f"CODIGO DE BARRAS: {numeros_inteiros}\n")
    
    impares = []
    pares = []
    i = 0
    
    while i < len(numeros_inteiros):
        if numeros_inteiros[i] % 2 != 0:
            impares.append(numeros_inteiros[i])
        else:
            pares.append(numeros_inteiros[i])
            
        i += 1
        
    result_impares = [number * 3 for number in impares]    
    result_pares = [number * 1 for number in pares]
    total = sum(result_impares) + sum(result_pares)
    
    code_verificator = total / 10
    
    print(f"NUMEROS IMPARES: {impares}\n")
    print(f"SOMA NUMEROS IMPARES: {sum(result_impares)}\n")
    print(f"NUMEROS PARES: {pares}\n")
    print(f"SOMA NUMEROS PARES: {sum(result_pares)}")
    print(f"TOTAL: {total}")
    print(f"CODIGO VERIFICADOR: {int(code_verificator)}")
    
#ean = ''.join(ean) 

code_ean_generator()