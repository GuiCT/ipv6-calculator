from ctypes import FormatError
from msilib import add_data
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
