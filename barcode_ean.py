from io import BytesIO
from random import randint
from barcode import EAN13
from barcode.writer import SVGWriter

def generate_ean13():
    # Começa com o prefixo '790 ou 789 no caso do Brasil'
    prefix = '790'

    # Gera 9 dígitos aleatórios para completar os 12 dígitos (excluindo o dígito de verificação)
    digits = [randint(0, 9) for _ in range(9)]
    
    # Transformando em tipo String e adicionando a uma variável
    numbers_of_digits = ''.join(map(str, digits))
    
    # Calcula o dígito de verificação
    all_digits = [int(digit) for digit in prefix + numbers_of_digits]
    
    # Números na posição impar do array
    odd_sum = sum(all_digits[::2])
        
    #Números na posição par do array
    even_sum = sum(all_digits[1::2])
        
    total = odd_sum + even_sum * 3
    check_digit = str((10 - (total % 10)) % 10)

    # Junta todos os dígitos para formar o código EAN-13 completo
    barcode = prefix + numbers_of_digits + check_digit

    return barcode

def generateSVGBarcode(code):
    rv = BytesIO()
    EAN13(code, writer=SVGWriter()).write(rv)    
    
    with open(f"{code}", "wb") as f:
        EAN13(str(code), writer=SVGWriter()).write(f)

if __name__ == '__main__':
    
    # Gera um exemplo de código de barras EAN-13 válido começando com '790'
    barcode = generate_ean13()
    generateSVGBarcode(barcode)
    print(f'Código de barras EAN-13: {barcode}')
