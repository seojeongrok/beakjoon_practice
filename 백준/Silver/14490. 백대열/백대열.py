n, m = map(int, input().split(":"))

def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

result = gcd(n, m)
print('%d:%d' %(n // result, m // result))