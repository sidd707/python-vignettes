# These following 4 exercises deal with the Fibonacci sequence.

import math
import decimal
from decimal import Decimal
from timeit import default_timer as timer

def fib(n):
    seq = [1, 2]
    for i in range(3, n+1):
        seq.append(seq[i-3] + seq[i-2])
    return seq

def real_fib(n):
    seq = [1, 1]
    for i in range(3, n+1):
        seq.append(seq[i-3] + seq[i-2])
    return seq

def gfs(a, b, n):
    seq = [a, b]
    for i in range(3, n+1):
        seq.append(seq[i-3] + seq[i-2])
    return seq

def fib_even_sum(maximum):
    last = 2
    lastlast = 1
    total = 2
    i = 3
    while i < 33:
        n = last + lastlast
        if n % 2 == 0:
            total += n
        lastlast = last
        last = n
        i += 1
    return total

def fib_num_digits(digits):
    last = 1
    lastlast = 1
    i = 3
    while True:
        n = last + lastlast
        if math.ceil(math.log(n,10)) == digits:
            return i
        lastlast = last
        last = n
        i += 1

def gfs_ratio(a, b, accuracy):
    phi = ((Decimal('1') + Decimal('5').sqrt())/Decimal('2')).quantize(accuracy)
    last = b
    lastlast = a
    i = 2
    while True:
        ratio = Decimal(str(last)) / Decimal(str(lastlast))
        if ratio.quantize(accuracy) == phi:
            return i
        n = last + lastlast
        lastlast = last
        last = n
        i += 1

# Part 1
# Fibonacci Sequence – The Fibonacci sequence is the sequence defined by starting
# with 1, 2, ... and producing each term by summing the previous two terms:
# 1, 2, 3, 5, 8, 13, 21, 34...
# Determine the 1000th Fibonacci number (note that we start with 1, 2, not 1, 1). 

start = timer()
seq = fib(1000)
end = timer()
print('Part 1: %f' % (end - start))
print('1000th Fibonacci number: %d\n' % seq[999])

# Part 2 -- Easy Way
# Fibonacci Sums – Using the same definition of the Fibonacci sequence as above,
# determine the sum of all even-valued terms in the sequence below 4,000,000. 

start = timer()
seq = fib(32)
total = sum(seq[1::3])
end = timer()
print('Part 2 (easy way): %f' % (end - start))
print('Sum of even Fibonacci numbers under 4 000 000: %d\n' % total)

 # Part 2 -- Fast Way


start = timer()
total = fib_even_sum(4000000)
end = timer()
print('Part 2 (fast way): %f' % (end - start))
print('Sum of even Fibonacci numbers under 4 000 000: %d\n' % total)

# Part 3 -- Straightforward Way
# Big Fibonacci – Lets consider a few more terms of the Fibonacci sequence,
# and slightly alter our above sequence to instead begin with 1, 1:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# Here we can see that the 7th term in the sequence is the first to have two digits
# and the 12th term in the sequence is the first to have three digits. What is the
# index of the first term to have 1000 digits?

start = timer()
n = fib_num_digits(1000)
end = timer()
print('Part 3 (straightforward way): %f' % (end - start))
print('First Fibonacci number with 1000 digits: %d\n' % n)

# Part 3 -- Tricky Way

start = timer()
seq = real_fib(5000)
n = next(i*4+7 for i, x in enumerate(seq[6::4])
         if math.ceil(math.log(x,10)) == 1000)
n = next(n-4+i for i, x in enumerate(seq[n-5:n])
         if math.ceil(math.log(x,10)) == 1000)
end = timer()
print('Part 3 (tricky way): %f' % (end - start))
print('First Fibonacci number with 1000 digits: %d\n' % n)

# Part 4 -- Straightforward Way

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
decimal.getcontext().prec = 18

start = timer()
n = gfs_ratio(1234, 567890, Decimal('1E-15'))
end = timer()
print('Part 4 (straightforward way): %f' % (end - start))
print('Terms for GFS(1234, 567890) to converge within 15 decimal places of phi: %d\n' % n)

# Part 4 -- Tricky Way

start = timer()
phi = Decimal('1.618033988749895')
accuracy = Decimal('1E-15')
seq = [Decimal(str(x)) for x in gfs(1234, 567890, 50)]
n = next(i+1 for i, x in enumerate(seq)
         if (x/seq[i-1]).quantize(accuracy)==phi)
end = timer()
print('Part 4 (tricky way): %f' % (end - start))
print('Terms for GFS(1234, 567890) to converge within 15 decimal places of phi: %d\n' % n)

print('Phi:\t1.618033988749895')
print('40/39:\t%s'%str(seq[39]/seq[38]))
print('39/38:\t%s\n'%str(seq[38]/seq[37]))

# Part 4 -- Challenge (Straightforward Way)
# Generalized Fibonacci and the Golden Ratio – It turns out that while the Fibonacci
# sequence is interesting because appears consistently in nature, one of its most
# interesting mathematical properties is not specific to the starting values of 1, 1
# or 1, 2.  Let's define GFS(a, b) to be a generalized Fibonacci sequence starting
# with terms a, b. For example, GFS(4, 11) = {4, 11, 15, 26, 41, ...}
# Here we'll also use the notation that GFS3(4, 11) = 15, where 3 indicates the 3rd
# term in the sequence. It turns out that any generalized Fibonacci sequence has the
# property that lim n→∞ GFSn+1 / GFSn = (1 + √5) / 2 which is also known as the
# Golden Ratio. Determine how many terms it takes GFS(1234, 567890) to converge to
# within 15 decimal places of accuracy to the Golden Ratio. (So according to the
# above definition, your answer would be n + 1). For an added challenge, find a
# module that will help you determine how many terms it takes to converge to within
# 100 decimal places of accuracy.

decimal.getcontext().prec = 103

start = timer()
n = gfs_ratio(1234, 567890, Decimal('1E-100'))
end = timer()
print('Part 4 (challenge, straightforward way): %f' % (end - start))
print('Terms for GFS(1234, 567890) to converge within 100 decimal places of phi: %d\n' % n)

# Part 4 -- Challenge (Tricky Way)

start = timer()
accuracy = Decimal('1E-100')
phi = ((Decimal('1') + Decimal('5').sqrt())/Decimal('2')).quantize(accuracy)
seq = [Decimal(str(x)) for x in gfs(1234, 567890, 250)]
n = next(i+1 for i, x in enumerate(seq)
         if (x/seq[i-1]).quantize(accuracy)==phi)
end = timer()
print('Part 4 (challenge, tricky way): %f' % (end - start))
print('Terms for GFS(1234, 567890) to converge within 100 decimal places of phi: %d\n' % n)

print('Phi:\t\t1.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911375')
print('244/243:\t%s'%str(seq[243]/seq[242]))
print('243/242:\t%s'%str(seq[242]/seq[241]))
