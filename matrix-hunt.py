# The following 5 exercises deal with the number in matrix-hunt-input.txt,
# treating it either as a 1000-digit number or 20x50 matrix.

from functools import reduce
from timeit import default_timer as timer

with open('matrix-hunt-input.txt') as f: data = f.read()
lines = data.split('\n')
number = ''.join(lines)
columns = [number[i::50] for i in range(50)]
digits = [int(x) for x in number]

# Part 1
# Maximal Product - Treating this as a 1000-digit number,
# determine the greatest possible product of 13 consecutive digits.

start = timer()
i = 0
maxProd = 0
maxSub = ''
maxIdx = 0
while i < len(number) - 12:
    sub = number[i:i+13]
    j = sub.rfind('0')
    if j != -1:
        i += j + 1
        continue
    prod = reduce(lambda x, y: int(x) * int(y), sub)
    if prod > maxProd:
        maxProd = prod
        maxSub = sub
        maxIdx = i
    i += 1
end = timer()
print('Part 1: %.20f' % (end - start))
print('%s, which starts at digit %d, has product %d\n' % (maxSub, maxIdx + 1, maxProd))

# Part 2
# Digit Counts - The string of digits "2094719482" has a total of four digits that
# are either 0,1, or 2. Treating this as a 20x50 matrix, determine the row that has
# the greatest total count of the digits 0, 1, 2.

start = timer()
cnt, idx = max([(x.count('0') + x.count('1') + x.count('2'), i)
            for i, x in enumerate(lines)])
end = timer()
print('Part 2: %.20f' % (end - start))
print('Row %d has %d digits that are 2 or less' % (idx + 1, cnt))
print(lines[idx] + '\n')

# Part 3
# Diagonal Products - Treating this as a 20x50 matrix, determine the smallest
# non-zero product of 5 digits that lie on a diagonal across the matrix.

start = timer()
mindiag = ''
minprod = 9**5+1
icoord = 0
jcoord = 0
forward = False
for i in range(50):
    for j in range(16):
        if i <= 45:
            diag = [lines[j+x][i+x] for x in range(5)]
            prod = reduce(lambda x, y: int(x) * int(y), diag)
            if prod > 0 and prod < minprod:
                mindiag = diag
                minprod = prod
                icoord = i
                jcoord = j
                forward = True
        if i >= 4:
           diag = [lines[j-x][i-x] for x in range(5)]
           prod = reduce(lambda x, y: int(x) * int(y), diag)
           if prod > 0 and prod < minprod:
               mindiag = diag
               minprod = prod
               icoord = i
               jcoord = j
               forward = False
end = timer()
print('Part 3: %.20f' % (end - start))
print('%s, the %s diagonal at (%d, %d), has product %d\n' % (''.join(mindiag), 'forward' if forward else 'backward', jcoord + 1, icoord + 1, minprod))

# Part 4
# Non-Decreasing Subsequence - Treating this as a 1000-digit number, determine the
# length of thelongest non-decreasing sequence of digits. For example, the sequence
# of digits 1112333344445 is a non-decreasing sequence of 13 digits since every digit
# is at least as large as the previous digit.

start = timer()
current = 0
best = 0
bestIdx = 0
last = 0
for i, n in enumerate(digits):
    if n >= last:
        current += 1
    else:
        if current > best:
            best = current
            bestIdx = i
        current = 1
    last = n
end = timer()
print('Part 4: %.20f' % (end - start))
print('%s, which starts at digit %d, has length %d\n' % (''.join(number[bestIdx-best:bestIdx]), bestIdx-best+1, best))

# Part 5
# Binary Extraction- Treating this as a 20x50 matrix, determine which column has the
# greatest value of a binary extraction subsequence. For example, if we took the
# column "3810817104", we could extract only the 1's and 0's in order, leaving us
# with "_ _ 1 0 _ 1 _ 1 0 _" → 10110 in binary, which converts to 22 in decimal.
# Therefore, the binary extraction value of this column is 22.

start = timer()
binary = [''.join([x for x in col if x == '0' or x == '1'])
          for col in columns]
val, idx = max([(int(x, 2), i) if x != '' else (0, i) for i, x in enumerate(binary)])
end = timer()
print('Part 5: %.20f' % (end - start))
print('Column %d reduces to %s, which is %d in decimal' % (idx+1, binary[idx], val))
