import math

class BinaryEncoder:

    @staticmethod
    def int_to_binary(num: int, width: int) -> str:
        return format(num, '0{}b'.format(width))

    @staticmethod
    def binary_to_int(binary: str) -> int:
        return int(binary, 2)
    
    def minimum_bits(n):
        if n == 0:
            return 1

        if n < 0:
            n = abs(n)

        if n == 1:
            return 1

        num_bits = math.floor(math.log2(n)) + 1
        return num_bits
