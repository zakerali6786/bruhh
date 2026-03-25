kw = {"int","float","if","else","while","return"}
op = "+-*/=<>&|"
sp = "(){}[],;"

code = ""
print("Enter code (END to stop):")
while True:
    l = input()
    if l == "END": break
    code += l + "\n"

k=i=o=s=0
seen=set()

words = code.replace('\n',' ').split()

for w in words:
    if w in kw:
        k+=1
    elif w.isalpha() and w not in seen:
        seen.add(w); i+=1

for ch in code:
    if ch in op: o+=1
    if ch in sp: s+=1

print("\nKeywords:",k)
print("Identifiers:",i)
print("Operators:",o)
print("Special chars:",s)
print("Lines:",code.count('\n'))