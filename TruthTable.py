def Conjunction(p, q):
    return p and q

def Disjunction(p, q):
    return p or q

def Conditional(p, q):
    return not p or q

def Biconditional(p, q):
    return p == q

def Negation(p):
    return not p

def printTableFunction1():
    print("p / r / -p and r")
    for p in [True, False]:
        for r in [True, False]:
            print(p, r, Conditional(Negation(p), r))

def printTableFunction2():
    print("p / r / p or r")
    for p in [True, False]:
        for r in [True, False]:
            print(p, r, Disjunction(p, r))

def printTableFunction3():
    print("p / q / r / not p / q or r / not p and (q or r)")
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                print(p, q, r, Negation(p), Disjunction(q, r), Conjunction(Negation(p), Disjunction(q, r)))

def printTableFunction4():
    print("p / q / r / not p / not q / not q or r / not p if (not q or r)")
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                print(p, q, r, Negation(p), Negation(q), Disjunction(Negation(q), r), Conditional(Negation(p), Disjunction(Negation(q), r)))

printTableFunction4()




    
