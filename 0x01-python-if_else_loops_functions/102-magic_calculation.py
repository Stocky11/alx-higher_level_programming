#!/usr/bin/python3
<<<<<<< HEAD


def magic_calculation(a, b):
"""Match bytecode provided by Holberton School."""
from magic_calculation_102 import add, sub

if a < b:
c = add(a, b)
for i in range(4, 6):
c = add(c, i)
return (c)

else:
return(sub(a, b))
=======
# 102-magic_calculation.py


def magic_calculation(a, b, c):
"""Match bytecode provided by Holberton School."""
if a < b:
return (c)
if c > b:
return (a + b)
return (a*b - c)
>>>>>>> 94c884206567d891e672b15d6a08b5753ed7e492

