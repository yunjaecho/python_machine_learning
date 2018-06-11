total_seconds = 7385
hours, remaining_seconds = divmod(total_seconds, 3600)
print(hours, remaining_seconds)
print(round(total_seconds/3600, 4))

from fractions import Fraction
total_seconds = Fraction(7385)
print(total_seconds)
hours = total_seconds / 3600
print(hours)
print(round(float(hours),4))
print(7385//3600)
print(7385.0//3600.0)