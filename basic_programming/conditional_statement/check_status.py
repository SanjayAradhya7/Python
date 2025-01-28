def checkStatus(a, b, flag):
    if a>=0 and b<0 or a<0 and b>=0 and not flag:
        return True
    elif a<0 and b<0 and flag:
        return True
    else:
        return False

print(checkStatus(5, -5, False))
print(checkStatus(-5, 5, False))
print(checkStatus(5, 5, True))   
print(checkStatus(-5, -5, True))
