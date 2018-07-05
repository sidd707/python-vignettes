# Source: https://fivethirtyeight.com/features/please-help-me-i-have-a-number-problem/
#
# Speaking of compulsive counting counts, I, too, have a problem. Whenever I see a
# string of digits — a license plate, a ZIP code … a stranger's PIN number — I try to
# turn them into a true mathematical equation by maintaining the digits' order and
# inserting symbols. For example, the ZIP code of my office is 10023. I could turn
# that into 1+0+0+2=3 or 1×0=0×23 (or many other equations).
#
# This game gets more complicated the more digits you have, and strings of four or
# five digits seem to be the sweet spot where there's a lot of fun to be had.
#
# Considering strings of all lengths and inserting only common mathematical
# symbols — ) ( + – × ÷ ^ = — what proportion of each string length has true
# mathematical equations lurking inside of it? (For example, for strings of length
# three, you'd consider the groups of digits 000, 001, ..., 999, trying to insert
# symbols into each one to find a correct equation. You'd find that 000 has many
# possibilities, whereas 129 has none. For strings of length four, you'd consider
# 0000 through 9999, and so on.) As the strings get longer, there's more you can do
# with them: Is there a string length where every possible string has a correct
# equation inside of it?

import re
import itertools

symbols = ['', '==', '+', '-', '*', '/', '**']
reg = re.compile(r'(^|[=+-/*])(0+)([1-9])')

unsafe = []

def safeEval(exp):
    global reg, unsafe
    exp = reg.sub(r'\1\3', exp)
    if exp.count('**') > 1:
        unsafe.append(exp)
        return False
    try: return eval(exp)
    except: return False

def permute(s,vals):
    if len(s) <= 1: return [s]
    suf = permute(s[1:],vals)
    p = []
    for op in vals:
        pre = s[0] + op
        p.extend([pre + x for x in suf])
    return p

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
    
def addParensEq(s):
    pieces = [addParensExp(x) for x in s.split('==')]
    return ['=='.join(x) for x in itertools.product(*pieces)]

p = [x for x in permute('999999', symbols) if '==' in x]
q = []
for x in p:
    q.extend(addParensEq(x))
print(len(q))
for x in q:
    if safeEval(x):
        print(x)
print('----------------------------')
print(unsafe[:10])
quit()

for i in range(2,6):
    num = [str(x).zfill(i) for x in range(10**i)]
    total = 0
    valid = 0
    for n in num:
        if int(n) % 100 == 0: print(n)
        p = [x for x in permute(n, symbols) if '==' in x]
        if i > 3:
            q = []
            for x in p:
                q.extend(addParensEq(x))
            p = q
        #c = 0
        for x in p:
            #c += 1
            if safeEval(x):
                valid += 1
                break
        #print("%d//%d: %s" % (int(n),c,x))
    prop = valid / len(num) * 100
    print('{}: {}%'.format(i, prop))
