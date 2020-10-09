def concat(s1, s2):
    if not s1:
        return s2
    return s1[0:1] + concat(s1[1:], s2)


def reverse(s1):
    if not s1:
        return s1
    return concat(reverse(s1[1:]), s1[0])
    

def prefix(s1, s2):
    if s1 == '' and s2 != '':
        return True
    if s1[:1] == s2[:1]:
        return prefix(s1[1:], s2[1:])
    return False


s1 = input()
s2 = input()

print(concat(s1, s2))
print(reverse(s1))
print(prefix(s1, s2))
