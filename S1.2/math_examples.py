#!/usr/bin/env python
# math_examples.py
# run as: python math_examples.py
# Author: Gavin Schlissel
# 2014_07_06
# 
# Demonstrate basic mathematical operations


# initialize variables
i=42
f=3.14159

# Here I used notation that is not described in the course material. I use the 
# prefix f_ for variables that are float type. This can be a useful way to
# remind yourself what type of variable you are dealing with.

# Add the variables
f_sum=i+f

# Subtract the variables
f_subtract=i-f

# Multiply the variables
f_multiply=i*f

# Divide the variables
f_divide=i/f

# Exponentiate the variables
f_expo=i**f

print "sum:" , f_sum
print "difference:", f_subtract
print "product:" , f_multiply
print "quotient:" , f_divide
print "exponent:" , f_expo
print

# Generate another example variable, and demonstrate addition shortcut
i_x = 1
print "x:" , i_x

i_x+=1
print "x:" , i_x

i_x+=8
print "x:" , i_x
