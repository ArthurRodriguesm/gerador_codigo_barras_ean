import random

def generate_ean13():
    # Começa com o prefixo '790'
    prefix = '790'

    # Gera 9 dígitos aleatórios para completar os 12 dígitos (excluindo o dígito de verificação)
    digits = [random.randint(0, 9) for _ in range(9)]

    # Calcula o dígito de verificação
    all_digits = [int(digit) for digit in prefix + ''.join(map(str, digits))]
    odd_sum = sum(all_digits[::2])
    even_sum = sum(all_digits[1::2])
    total = odd_sum + even_sum * 3
    check_digit = (10 - (total % 10)) % 10

    # Junta todos os dígitos para formar o código EAN-13 completo
    barcode = prefix + ''.join(map(str, digits)) + str(check_digit)

    return barcode

if __name__ == '__main__':
    # Gera um exemplo de código de barras EAN-13 válido começando com '790'
    barcode = generate_ean13()
    print(f'Código de barras EAN-13 gerado: {barcode}')
