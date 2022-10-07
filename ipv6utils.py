import re

# Compilando regex para validar IPv6
# Abrindo o arquivo ipv6regex.txt que contém o regex
with open('ipv6regex.txt') as f:
    ipv6regex = re.compile(f.read())

def ipv6_as_bytes(ipv6_str: str) -> bytes:
    # Se input não for válido, raise um ValueError
    if not ipv6regex.fullmatch(ipv6_str):
        raise ValueError('ipv6 inserido não é válido')
    # Separando em grupos de hexadecimal
    hex_groups = ipv6_str.split(':')
    # Tratando os espaços vazios causados por :: (ao fim ou no meio do endereço)
    if '' in hex_groups:
        # Ao fim
        if hex_groups[-1] == '':
            del hex_groups[-1]
        # Índice em que ocorre o ::
        i = hex_groups.index('')
        del hex_groups[i]
        # Número de grupos faltantes
        remaining_groups = 8 - len(hex_groups)
        # Preenche o espaço vazio com quartetos '0000'
        hex_groups = hex_groups[:i] + remaining_groups * ['0000'] + hex_groups[i:]
    # Realizando um zero-fill para cada quarteto
    hex_groups = [group.zfill(4) for group in hex_groups]
    # Agora é possível transformar cada quarteto em um array de bytes
    # e transformar o endereço originalmente expresso em string em um
    # array de 128 bits (16 bytes)
    res_bytearray = bytearray()
    # Iterando sobre a lista
    for group in hex_groups:
        # Convertendo hexadecimal em inteiro
        group_as_integer: int = int(group, 16)
        # Convertendo em bytes e concatenando ao início do bytearray
        res_bytearray += bytearray(group_as_integer.to_bytes(2, 'big'))
    # Retorna o endereço final em bytes
    return bytes(res_bytearray)

def ipv6_as_str(ipv6_byt: bytes) -> str:
    pass

if __name__ == '__main__':
    ipv6_as_bytes('2001::')