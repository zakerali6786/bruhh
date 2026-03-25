grammar = {}
n = int(input("No. of productions: "))

# ---------- INPUT ----------
for _ in range(n):
    l = input().split("->")
    left = l[0].strip()
    right = l[1].split("|")
    grammar[left] = [r.strip().split() for r in right]

FIRST, FOLLOW = {}, {}

# ---------- FIRST ----------
def first(X):
    if X not in grammar:
        return {X}
    if X in FIRST:
        return FIRST[X]

    FIRST[X] = set()
    for prod in grammar[X]:
        for sym in prod:
            f = first(sym)
            FIRST[X] |= (f - {"#"})
            if "#" not in f:
                break
        else:
            FIRST[X].add("#")
    return FIRST[X]

# ---------- FOLLOW ----------
def follow(X):
    if X in FOLLOW:
        return FOLLOW[X]

    FOLLOW[X] = set()
    if X == list(grammar.keys())[0]:
        FOLLOW[X].add("$")

    for lhs in grammar:
        for prod in grammar[lhs]:
            for i in range(len(prod)):
                if prod[i] == X:
                    if i+1 < len(prod):
                        f = first(prod[i+1])
                        FOLLOW[X] |= (f - {"#"})
                        if "#" in f:
                            FOLLOW[X] |= follow(lhs)
                    else:
                        if lhs != X:
                            FOLLOW[X] |= follow(lhs)
    return FOLLOW[X]

# ---------- COMPUTE ----------
for nt in grammar:
    first(nt)
for nt in grammar:
    follow(nt)

# ---------- TABLE ----------
table = {nt:{} for nt in grammar}

for lhs in grammar:
    for prod in grammar[lhs]:
        fset = set()
        for sym in prod:
            f = first(sym)
            fset |= (f - {"#"})
            if "#" not in f:
                break
        else:
            fset.add("#")

        for t in fset - {"#"}:
            table[lhs][t] = prod

        if "#" in fset:
            for t in FOLLOW[lhs]:
                table[lhs][t] = prod

# ---------- OUTPUT ----------
print("\nFIRST:")
for nt in grammar:
    print(nt, FIRST[nt])

print("\nFOLLOW:")
for nt in grammar:
    print(nt, FOLLOW[nt])

print("\nLL(1) TABLE:\n")

terms = list(set(t for nt in table for t in table[nt]))

print("{:<6}".format("NT"), end="")
for t in terms:
    print("{:<12}".format(t), end="")
print()

for nt in grammar:
    print("{:<6}".format(nt), end="")
    for t in terms:
        if t in table[nt]:
            print("{:<12}".format(nt+"->"+" ".join(table[nt][t])), end="")
        else:
            print("{:<12}".format(""), end="")
    print()