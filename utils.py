## Taken/credit from ChatGPT

class Utils:
    @staticmethod
    def reversed_number(number):
        if isinstance(number, int):
            if number >= 0:
                reversed_num = int(str(number)[::-1])
            else:
                reversed_num = -int(str(abs(number))[::-1])
            return reversed_num
        else:
            raise ValueError("Input must be an integer")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            binary = bin(number)[2:]
            octal = oct(number)[2:]
            return binary, octal
        else:
            raise ValueError("Input must be an integer")
        
utils_temp = Utils()

