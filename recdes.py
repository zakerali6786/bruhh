s = input("Enter string: ")
i = 0

def E():
    global i
    if T(): return E1()

def E1():
    global i
    if i < len(s) and s[i] == '+':
        i += 1
        if T(): return E1()
    return True

def T():
    global i
    if F(): return T1()

def T1():
    global i
    if i < len(s) and s[i] == '*':
        i += 1
        if F(): return T1()
    return True

def F():
    global i
    if i < len(s) and s[i] == 'i':
        i += 1
        return True
    elif i < len(s) and s[i] == '(':
        i += 1
        if E() and i < len(s) and s[i] == ')':
            i += 1
            return True
    return False

if E() and i == len(s):
    print("Accepted")
else:
    print("Rejected")


gedit lexana.py
python3 lexana.py