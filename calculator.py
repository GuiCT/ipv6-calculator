from math import ceil, log

CIDR_MIN = 1
CIDR_MAX = 127

# Retorna a OR mask para calcular um endereço IPV6
# Precisa da quantidade de bits ignorados (inalterados)
# e o valor dos bits alterados
def or_mask(unchanged_bits: int, changed_bits: str) -> int:
    remaining_bits = 128 - unchanged_bits - len(changed_bits)
    mask_as_str = changed_bits + '0'*remaining_bits
    return int(mask_as_str, 2)

# Função que lê bytes em big endian e retorna um inteiro
bytes_as_int = lambda byt: int.from_bytes(byt, 'big')

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
        raise ValueError(f"o CIDR inserido é inválido:\n{e}")
    if not (cidr >= CIDR_MIN and cidr <= CIDR_MAX):
        raise ValueError(f"valor do CIDR deve estar entre {CIDR_MIN} e {CIDR_MAX}")
    # Tratamento do IP, TODO
    return address, cidr