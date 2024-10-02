def set_union(A, B) :
    return A.union(B)

def list_union(A, B) :
    result = []
    for x in A:
        if x not in B:
            result = result + list(str(x))
    for x in B:
        result = result + list(str(x))
    return result

def set_intersection(A,B) :
    result = []
    for x in A:
        if x in B:
            result = result + list(str(x))
    return result

def set_difference(A,B) :
    result = []
    for x in A:
        if x not in B:
            result = result + list(str(x))
    for x in B:
        if x not in A:
            result = result + list(str(x))
    return result
        
def set_isSubSet(A, B) :
    result = []
    for x in A:
        if x in B:
            result = result + list(str(x))
    if result == B :
        print("is Sub Set")
    else :
        print("is not Sub Set")

def isProperSubset(A, B) :
    result = []
    for x in A:
        if x in B:
            result = result + list(str(x))
    if result == A:
        print("is proper subset")
    else:
        print("is not a proper subset")

    
        
    

def Test01() :
    A = {1, 2, 8}
    B = {1, 2, 3, 4, 5}
    print(set_union(A, B))
    A = [1, 2, 8]
    B = [1, 2, 3, 4, 5]
    print(list_union(A, B))
    print(set_intersection(A, B))
    print(set_difference(A, B))
    print(set_isSubSet(A, B))
    print(isProperSubset(A, B))


Test01()