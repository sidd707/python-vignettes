# Source: https://fivethirtyeight.com/features/please-help-me-i-have-a-number-problem/
#
# Speaking of compulsive counting counts, I, too, have a problem. Whenever I see a
# string of digits -- a license plate, a ZIP code, a stranger's PIN number -- I try
# to turn them into a true mathematical equation by maintaining the digits' order and
# inserting symbols. For example, the ZIP code of my office is 10023. I could turn
# that into 1+0+0+2=3 or 1*0=0*23 (or many other equations).
#
# This game gets more complicated the more digits you have, and strings of four or
# five digits seem to be the sweet spot where there's a lot of fun to be had.
#
# Considering strings of all lengths and inserting only common mathematical
# symbols -- ) ( + * / ^ = -- what proportion of each string length has true
# mathematical equations lurking inside of it? (For example, for strings of length
# three, you'd consider the groups of digits 000, 001, ..., 999, trying to insert
# symbols into each one to find a correct equation. You'd find that 000 has many
# possibilities, whereas 129 has none. For strings of length four, you'd consider
# 0000 through 9999, and so on.) As the strings get longer, there's more you can do
# with them: Is there a string length where every possible string has a correct
# equation inside of it?

import re
import itertools

symbols = ['', '==', '+', '-', '*', '/'] # The puzzle should include ** but I need to
                                         # figure out a way to deal with large
                                         # exponentials like 9 ** 9 ** 9
reg = re.compile(r'(^|[=+-/*])(0+)([1-9])')

def safeEval(exp):
    global reg
    exp = reg.sub(r'\1\3', exp) # Trim leading zeros
    try: return eval(exp)
    except: return False

# This function finds every permutation of operators placed between the digits
def permute(s, vals):
    if len(s) <= 1: return [s]
    suf = permute(s[1:], vals)
    p = []
    for op in vals:
        pre = s[0] + op
        p.extend([pre + x for x in suf])
    return p

# This function determines all the ways parentheses may be added to an expression
def addParensExp(s):
    pieces = re.split('(\+|-|\*\*|/|\*)', s)
    if len(pieces) == 1: return pieces
    p = []
    for i in range(1, len(pieces), 2):
        pre = addParensExp(''.join(pieces[:i]))
        suf = addParensExp(''.join(pieces[i+1:]))
        for x in pre:
            for y in suf:
                p.append('(' + x + ')' + pieces[i] + '(' + y + ')')
    return p

# This function determines all the ways parentheses may be added to an equation
def addParensEq(s):
    pieces = [addParensExp(x) for x in s.split('==')]
    return ['=='.join(x) for x in itertools.product(*pieces)]

# Start with 2 digit numbers and work up to 4 digits
for i in range(2,5):
    num = [str(x).zfill(i) for x in range(10**i)] # Creates list of all numbers with i digits
    valid = 0
    for n in num:
        p = [x for x in permute(n, symbols) if '==' in x]
        if i > 3: # Only 4+ digit numbers can be altered by parentheses
            q = []
            for x in p:
                q.extend(addParensEq(x))
            p = q
        for x in p:
            if safeEval(x):
                valid += 1
                break
    prop = float(valid) / len(num) * 100
    print('{}: {}%'.format(i, prop))
