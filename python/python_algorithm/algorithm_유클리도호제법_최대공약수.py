'''
input: 192 162

output: 6
두수의 최대공약수
'''

def gcd(a, b):
    print(a,b,a%b)
    if a % b !=0:
        return gcd(b,a%b)
    else:
        return b

print(gcd(192,162))

