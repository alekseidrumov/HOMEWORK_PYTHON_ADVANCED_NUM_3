x_string = 'string'
y_string = 'set'
x_set = set(x_string)
y_set = set(y_string)
z = x_set.difference(y_set) 
print(z)