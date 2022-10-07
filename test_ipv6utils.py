import ipv6utils
import socket

def test_ipv6_str_to_bytes_1():
    assert ipv6utils.ipv6_as_bytes('2001::') == socket.inet_pton(socket.AF_INET6, '2001::')

def test_ipv6_str_to_bytes_2():
    assert ipv6utils.ipv6_as_bytes('2001::abcd') == socket.inet_pton(socket.AF_INET6, '2001::abcd')

def test_ipv6_str_to_bytes_3():
    assert ipv6utils.ipv6_as_bytes('2001:0::1234:0000') == socket.inet_pton(socket.AF_INET6, '2001:0::1234:0000')
