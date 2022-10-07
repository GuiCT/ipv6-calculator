import re

# Compilando regex para validar IPv6
# Abrindo o arquivo ipv6regex.txt que contém o regex
with open('ipv6regex.txt') as f:
    ipv6regex = re.compile(f.read())

def ipv6_as_bytes(ipv6_str: str) -> bytes:
    pass

def ipv6_as_str(ipv6_byt: bytes) -> str:
    pass