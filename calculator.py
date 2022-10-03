from socket import inet_pton, AF_INET6, error as socket_error

class ipv6address:
    @staticmethod
    def as_hexquartet(address: bytes):
        pass

    @staticmethod
    def as_string(address: bytes):
        pass

    @staticmethod
    def as_bytes(address: str):
        pass

    @staticmethod
    def check_ipv6_string(input: str) -> bool:
        try:
            inet_pton(AF_INET6, input)
            return True
        except socket_error:
            return False