# import decimal
# print(decimal.Decimal("2.5"))
# print(decimal.Decimal("26.5").quantize(decimal.Decimal("10"),decimal.ROUND_CEILING))
# print(round(2.5))
from decimal import Decimal, ROUND_HALF_UP

number1 = Decimal('3.14159')
rounded_number1 = number1.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
print(rounded_number1)  # Output: 3.14

number2 = Decimal('5.678')
rounded_number2 = number2.quantize(Decimal('1'))
print(rounded_number2)  # Output: 6

number3 = Decimal('27')
rounded_number3 = number3.quantize(Decimal('10'), rounding=ROUND_HALF_UP)
print(rounded_number3)  # Output: 30
