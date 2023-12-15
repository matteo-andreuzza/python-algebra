a = ''
b = ''

def molt(x,y):
    q = ''
    q2 = ''
    w = ''
    w2 = ''
    for i in x:
        try:
            if type(int(i)) == int:
                q += i
        except ValueError:
            q2 += i
    for i in y:
        try:
            if type(int(i)) == int:
                w += i
        except ValueError:
            w2 += i
    return str((int(q)*int(w))) + q2 + w2
op = ['-']
num = ['1','2','3','4','5','6','7','8','9']
def sum(x,y):
    q = ''
    q2 = ''
    w = ''
    w2 = ''
    c = 0
    if x[0] != "-" and x[0] not in num:
        t = list(x)
        t.insert(0, '1')
        x = ''
        for z in t:
            x += str(z)
        if y[0] != "+" or y[0] != "":
            t = list(y)
            t.insert(0, '1')
        y = ''
        for z in t:
            y += str(z)
    for i in x:
        try:
            if i == '-':
                continue
            if type(int(i)) == int and x[c] == '-':
                q += '-'+i
            else:
                q += i
        except ValueError:
            q2 += i
        c = c+1
    c = 0
    i = 0
    for i in y:
        try:
            if i == '-':
                continue
            if type(int(i)) == int and y[c] == '-':
                w += '-'+i
            else:
                w +=i
            
        except ValueError:
            w2 += i
        c = c+1
    if q2 == w2:
        return str((int(q)+int(w))) + q2
    else:
        return 'impossibile sommare termini con lettere diverse'
g1 = input("inserire primo termine... ")
g2 = input("inserire secondo termine... ")
print("somma " + str(sum(g1, g2)))
