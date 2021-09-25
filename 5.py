def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

num_one = int(input())
num_two = int(input())
if num_one == 0:
    print(num_two)
else:
    print(gcd(num_one, num_two))