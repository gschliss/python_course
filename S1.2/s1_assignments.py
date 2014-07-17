#!/usr/bin/env python
# s1_assignments.py
# run as: python s1_assignments.py
# Author: Gavin Schlissel
# 2014_07_08
#
# Section 1 assignments

# Demonstrate division and demonstrate problems with casting from
# user input

print "------- ratio --------"
# read in two numbers from the user
s_1 = raw_input("Input the first number ")
s_2 = raw_input("Input the second number ")

# Cast variables to float type
f_1 = float(s_1)
f_2 = float(s_2)

# calcualte the ratio
f_ratio = f_1 / f_2

# Print the result
print "The ratio is %5.2f" % (f_ratio)


# Ways to break the program:
# If s_2 is 0
# If either input contains a non-numeric character
# If either input contains multiple decimal points (non-valid number format)
# If either input contains a formula instead of an integer
# If the first input overruns the float type (max 1.7976931348623157e+308)
# If either input is blank

# Sum and mean

print "------- Sum and Mean --------"
f_1 = float(raw_input("Input the first number "))
f_2 = float(raw_input("Input the second number "))
f_3 = float(raw_input("Input the third number "))
f_4 = float(raw_input("Input the fourth number "))
f_5 = float(raw_input("Input the fifth number "))

print "The sum is %2.2f" % (f_1+f_2+f_3+f_4+f_5)
print "The mean is %2.2f" % ((f_1+f_2+f_3+f_4+f_5)/5)


# Swap
print "------------ Swap -----------"
s_input1 = raw_input("Input a string ")
s_input2 = raw_input("Input another string ")
foo = s_input1
s_input1 = s_input2
s_input2 = foo
print "input1: %s , input2: %s" % (s_input1 , s_input2)


print "------------ quick swap -----------"
s_input1 = raw_input("Input a string ")
s_input2 = raw_input("Input another string ")
s_input1 , s_input2 = s_input2 , s_input1
print "input1: %s , input2: %s" % (s_input1 , s_input2)


print "------------ index-tastic -----------"
i_num_digits = int(raw_input("How many digits should I expect? "))
s_num_sequence = raw_input("Input a sequence of five numbers separated by spaces, each with %s digits " % (i_num_digits))
f_sum = (float(s_num_sequence[0:(i_num_digits)]) +
         float(s_num_sequence[(i_num_digits+1):(2*i_num_digits+1)]) + 
         float(s_num_sequence[2*i_num_digits+2:3*i_num_digits+2]) +
         float(s_num_sequence[3*i_num_digits+3:4*i_num_digits+3]) +
         float(s_num_sequence[4*i_num_digits+4:5*i_num_digits+4]))
print "The sum is %f " % (f_sum)
print "The mean is %f " % (f_sum / 5)


print "------------ escape -----------"
print "'''hello \"world\", if that is your real name.\n That's World, to you'''"
