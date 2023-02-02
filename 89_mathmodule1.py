import math
print("\n checks 2 values are close to eeach other")
print(math.isclose(1.223,1.223))
print(math.isclose(1.223,1.24))

print("\n check wheather the no. is finite or not")
print(math.isfinite(2000))
print(math.isfinite(-45.34))
print(math.isfinite(+45.34))
print(math.isfinite(math.inf))
print(math.isfinite(float("nan")))
print(math.isnan(float("inf")))
print(math.isfinite(-math.inf))

print("\n check value is NAN not a no.or not")

print(math.isnan(56))
print(math.isnan(-45.34))
print(math.isnan(45.34))
print(math.isnan(math.inf))
print(math.isnan(float("nan")))
print(math.isnan(float("inf")))
print(math.isnan(float("-inf")))
print(math.isnan(math.nan))

print("\n prints log values")

print(math.log(2.783))
print(math.log(2))
print(math.log(1))

print("\n power values")
print(math.pow(9,3))

print("\n convert degree value to radians")
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))

print("\n return the product of all the element in an iterable")
sequence=(2,2,2)
print(math.prod(sequence))

print("\n return the remainder")
print(math.remainder(9,2))
print(math.remainder(9,3))
print(math.remainder(18,4))

print("\n returns the truncated integer parts of a number")
print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(-99.29))
