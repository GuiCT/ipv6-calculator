from audioop import add
from math import ceil, log

from ipv6utils import ipv6_as_bytes, ipv6_as_str

CIDR_MIN = 0
CIDR_MAX = 127

# Retorna a OR mask para calcular um endereço IPV6
# Precisa da subnetmask do endereço em CIDR
# e o valor dos bits alterados
def or_mask(cidr: int, changed_bits: str) -> int:
    remaining_bits = 128 - cidr
    mask_as_str = changed_bits + '0'*remaining_bits
    return int(mask_as_str, 2)

# Função que lê bytes em big endian e retorna um inteiro
def bytes_as_int(byt: bytes):
    return int.from_bytes(byt, 'big')

# Função que lê um inteiro e retorna 16 bytes em big endian
def int_as_bytes(integer: int):
    return int.to_bytes(integer, 16, 'big')

# Função que calcula passos leftmost e rightmost e os retorna em listas.
def rightmost_leftmost_steps(
    number_of_subnets: int
) -> tuple[list[str], list[str]]:
    # Menor potência de 2 maior que number_of_subnets e seu expoente
    exponent = ceil(log(number_of_subnets, 2))
    # Então cada passo terá (exponent) bits
    rightmost_list = list() # Endereços gerados utilizando rightmost
    leftmost_list = list() # Endereços gerados utilizando leftmost
    for i in range(number_of_subnets):
        rightmost = format(i, f'0{exponent}b')
        leftmost = rightmost[::-1] # Leftmost é o inverso do rightmost
        rightmost_list.append(rightmost)
        leftmost_list.append(leftmost)
    return (rightmost_list, leftmost_list)

def ipv6_cidr_treatment(ipv6_address: str) -> tuple[bytes, int]:
    address, cidr = ipv6_address.split('/')
    # Tratamento do CIDR, verifica se é um número e está dentro do intervalo
    try:
        cidr = int(cidr)
    except ValueError as e:
        raise ValueError(e)
    if not (cidr >= CIDR_MIN and cidr <= CIDR_MAX):
        raise ValueError(f"valor do CIDR deve estar entre {CIDR_MIN} e {CIDR_MAX}")
    # Tratamento do IP
    try:
        address = ipv6_as_bytes(address)
    except ValueError as e:
        raise ValueError(e)
    return address, cidr

if __name__ == '__main__':
    try:
        # Até entrada ser válida
        while True:
            untreated_input = input('Insira um IP no formato IPv6 com um CIDR: ')
            try:
                ipv6_bytes, cidr = ipv6_cidr_treatment(untreated_input)
            except ValueError as e:
                print(f'Input inválido: {e}\nPor favor tente novamente...')
                continue
            # Quantas subnets, até entrada ser válida
            while True:
                try:
                    subnet_amount = int(input('Insira a quantidade de sub-redes a ser geradas: '))
                    # CIDR das redes resultantes: CIDR original + expoente da potência de 2
                    exponent = ceil(log(subnet_amount, 2))
                    subnet_cidr = cidr + exponent
                    # Se o CIDR resultante for maior que 128, pedir novo valor
                    if subnet_cidr > 128:
                        print('O bloco não pode ser divido nessa quantidade de sub-redes, insira um valor menor.')
                        continue
                except ValueError:
                    print('Valor deve ser um inteiro.')
                else:
                    break
            # Máscaras rightmost e leftmost
            rightmask, leftmask = rightmost_leftmost_steps(subnet_amount)
            # Convertendo IP original em inteiro para aplicar máscaras OR
            ipv6_integer = bytes_as_int(ipv6_bytes)
            # Aplicando máscaras OR compostas pelas máscaras leftmost e rightmost
            # Guardando resultados em lista
            leftaddresses = list()
            rightaddresses = list()
            for i in range(len(rightmask)):
                # Leftmost
                leftaddress_int = ipv6_integer | or_mask(subnet_cidr, leftmask[i])
                leftaddresses.append(int_as_bytes(leftaddress_int))
                # Rightmost
                rightaddress_int = ipv6_integer | or_mask(subnet_cidr, rightmask[i])
                rightaddresses.append(int_as_bytes(rightaddress_int))
            # Printando rightmost
            print('Divisão de endereços utilizando rightmost:')
            for i, address in enumerate(rightaddresses):
                print(f'{i}: {ipv6_as_str(address)}')
            # Printando leftmost
            print('Divisão de endereços utilizando leftmost:')
            for i, address in enumerate(leftaddresses):
                print(f'{i}: {ipv6_as_str(address)}')
    except KeyboardInterrupt:
        exit(0)