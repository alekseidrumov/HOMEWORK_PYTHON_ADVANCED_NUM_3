c = [2,5,6,4,3]
def min(c, s, smallest):
    if c[s] < smallest:
        smallest = c[s]
    if s == len(c) - 1:
        return smallest
    else:
        return min(c, s+1,smallest)

print(min(c,0,c[0]))
