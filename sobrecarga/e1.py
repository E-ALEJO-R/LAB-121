from fractions import Fraction

"""
1) Crear una clase Fraction, donde que se puedan realizar las siguientes operaciones:
    a) Para sumar sobrecargar el operador +.
    b) Para restar sobrecargar el operador -.
    c) Para multiplicar sobrecargar el operador *.
"""


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        # if not isinstance((numerator, denominator), int):
        #     raise Exception(f"solo permitido número de tipo {int}")
        self.__numerator = numerator
        # if denominator == 0:
        #     raise Exception(f"el denominador no puede ser cero")
        self.__denominator = denominator

    @property
    def numerator(self) -> int:
        return self.__numerator

    @numerator.setter
    def numerator(self, value: int):
        self.__numerator = value

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, value: int):
        self.__denominator = value

    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other: Fraction) -> Fraction:
        mcm = Fraction.__mcm(self.denominator, other.denominator)
        dif_self = int(mcm / self.denominator)
        dif_other = int(mcm / other.denominator)
        numerator_result = (dif_self * self.numerator) + (dif_other * other.numerator)
        return Fraction(numerator_result, mcm)

    def __sub__(self, other: Fraction) -> Fraction:
        mcm = Fraction.__mcm(self.denominator, other.denominator)
        dif_self = int(mcm / self.denominator)
        dif_other = int(mcm / other.denominator)
        numerator_result = (dif_self * self.numerator) - (dif_other * other.numerator)
        return Fraction(numerator_result, mcm)

    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.__numerator * other.numerator,
            self.__denominator * other.denominator
        )

    @staticmethod
    def __mcd(a, b) -> int:
        while b != 0:
            tmp = b
            b = a % b
            a = tmp
        return int(a)

    @staticmethod
    def __mcm(a, b) -> int:
        return int((a * b) / Fraction.__mcd(a, b))


if __name__ == '__main__':
    f1 = Fraction(4, 7)
    f2 = Fraction(2, 3)

    print(f"F1 = {f1}, F2 = {f2}")

    print("suma:", f1 + f2)
    print("resta:", f1 - f2)
    print("multiplicación:", f1 * f2)
