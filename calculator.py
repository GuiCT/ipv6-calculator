from socket import inet_pton, inet_ntop, AF_INET6, error as socket_error

# Retorna o IPv6 inserido na forma de bytes
# Caso seja inválido, indica um
def ipv6_as_bytes(address_as_string: str) -> bytes:
    try:
        return inet_pton(AF_INET6, address_as_string)
    except socket_error:
        raise ValueError("O Endereço IPv6 inserido é inválido.")

# Retorna o IPv6 na forma de string
def ipv6_as_string(address_as_bytes: bytes) -> str:
    return inet_ntop(AF_INET6, address_as_bytes)

# Retorna a OR mask para calcular um endereço IPV6
# Precisa da quantidade de bits ignorados (inalterados)
# e o valor dos bits alterados
def or_mask(unchanged_bits: int, changed_bits: str) -> int:
    remaining_bits = 128 - unchanged_bits - len(changed_bits)
    mask_as_str = changed_bits + '0'*remaining_bits
    return int(mask_as_str, 2)

# Função que lê bytes em big endian e retorna um inteiro
bytes_as_int = lambda byt: int.from_bytes(byt, 'big')

# Função que calcula passos leftmost e rightmost e os retorna em uma lista.
def rightmost_leftmost_steps(number_of_subnets: int) -> list[str]:
    pass