def forall(pred, iterable):
    for el in iterable:
        if not pred(el):
            return False
    return True

def exists(pred, iterable):
    for el in iterable:
        if pred(el):
            return True
    return False

def atleast(n, pred, iterable):
    counter = 0
    for el in iterable:
        if pred(el):
            counter += 1
            if counter >= n:
                return True
    return False

def atmost(n, pred, iterable):
    counter = 0
    for el in iterable:
        if pred(el):
            counter += 1
            if counter > n:
                return False
    return True