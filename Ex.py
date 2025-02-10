from itertools import *
# Задание 8
k = 0
for x in product('0123456789ABCDEF', repeat = 5):
    s = ''.join(x)
    if s[0]!='0':
        for x in '123456789': s = s.replace(x,'0')
        if s.count('0')==1:
            k+=1
print(k)

print('')

# Задание 12

for n in range(4,10001):
    s = '9'+n*'6'
    while '666' in s or '9909' in s or '66' in s:
        s = s.replace('666','999',1)
        s = s.replace('9909','6',1)
        s = s.replace('66','0',1)
        if len(s)==10:
            print(n)
        break
print('')

print('')

# Задание 19-21

def f(s,m,p):
    if s>=131: return m%2==0
    if m==0: return 0
    h = []
    if p!='+2': h += [f(s+2,m-1, '+2')]
    if p!='+3': h += [f(s+3,m-1, '+3')]
    if p!='*2': h += [f(s*2,m-1, '*2')]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1,131) if f(s,2,'')])
print('20)', [s for s in range(1,131) if not f(s,1,'') and f(s,3,'')])
print('21)', [s for s in range(1,131) if not f(s,2,'') and f(s,4,'')])
